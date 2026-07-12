openapi: 3.0.0
info:
  title: 'Freemius API'
  description: "\nWelcome to the Freemius API Documentation!\n\nYou can use our API to access Freemius API endpoints, which can get information on various aspects of Freemius.\n\n- Manage products.\n- Manage license verifications.\n- Create custom integration with your SaaS.\n\nIf you're using Freemius for a WordPress product, please check out our official [SDK](https://github.com/Freemius/wordpress-sdk).\n\n## Bearer Token Auth\n\nFreemius API supports Bearer Token authentication for product-specific operations.\n\nTo retrieve your API token:\n\n1. Go to the [Freemius Developer Dashboard](https://dashboard.freemius.com/).\n2. Open the Settings page of the relevant product.\n3. Click the API & Keys tab.\n4. Copy the API Bearer Authorization Token from the UI.\n\nUse this token by including it in the `Authorization` header of your API requests:\n\n```http\nAuthorization: Bearer {api_token}\n```\n\nBearer tokens are **scoped to a specific product**. This means they can only be used with endpoints under the `/products/{product_id}/` namespace. For example:\n\n```http\nGET /products/12345/users.json\nAuthorization Bearer {api_token}\n```\n\nRequests to endpoints outside the product scope will result in an authorization error.\n\n## Other Scopes and Authentication\n\nThe Freemius API is organized around different **scopes**, based on the top-level entity of the operation:\n\nFor example, let's say you want to list all payments of a product. This operation can be done in several scopes:\n\n- **Product Scope**: `/products/{product_id}/payments.json`.\n- **Developer Scope**: `/developers/{developer_id}/products/{product_id}/payments.json`.\n\nOn the other hand, if a user would want to list their payment, then endpoint will be scoped to the user:\n\n- **User Scope**: `/users/{user_id}/payments.json`.\n\nSome operations can be done from a particular scope only. For example only a developer can update a plan of a product or create a new plan. So the following operations will work:\n\n- **Update Plan**: POST `/developers/{developer_id}/products/{product_id}/plans/{plan_id}.json`\n- **Create Plan**: POST `/developers/{developer_id}/products/{product_id}/plans.json`\n\nIf you try to perform the same operation on a product scope, it will return an error. The scopes provides a way to control access and permissions for different entities in the Freemius ecosystem.\n\nCurrently, **Bearer Token authentication is supported for product scope only**. If you need access to endpoints in others scopes, use the secret-key based authentication with the following SDKs:\n\n- [PHP SDK]( https://github.com/Freemius/freemius-php-sdk)\n- [NodeJS SDK](https://github.com/Freemius/freemius-node-sdk)\n\nFor most use cases, managing your products, licenses, and customers through the [Developer Dashboard](https://dashboard.freemius.com) or [Customer Portal](https://customers.freemius.com) provides all the necessary capabilities.\n"
  termsOfService: 'https://freemius.com/terms/'
  contact:
    name: 'Freemius Support'
    url: 'https://freemius.com'
    email: support@freemius.com
  license:
    name: Proprietary
    url: 'https://freemius.com/terms/'
  version: '1.0'
servers:
  -
    url: 'https://api.freemius.com/v1'
    description: 'Production API'
  -
    url: 'http://api.freemius-local.com:8080/v1'
    description: 'Local development API'
    x-remove-from-doc: true
    x-internal: true
paths:
  '/developers/{developer_id}/bank_account/{bank_account_id}.json':
    get:
      tags:
        - Developers
      summary: 'Retrieve bank account'
      description: 'Retrieve the developer''s bank account.'
      operationId: developers/retrieve-bank-account
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/BankAccount'
        '400':
          $ref: '#/components/responses/400'
        '401':
          $ref: '#/components/responses/401'
        '402':
          $ref: '#/components/responses/402'
        '404':
          $ref: '#/components/responses/404'
      security:
        -
          ApiAuthFSACookie: []
        -
          ApiAuthFSAHeader: []
      x-remove-from-doc: true
      x-internal: true
    parameters:
      -
        $ref: '#/components/parameters/developer_id'
      -
        $ref: '#/components/parameters/bank_account_id'
  '/developers/{developer_id}/login.json':
    post:
      tags:
        - Developers
      summary: 'Log in'
      description: "\nCall this endpoint with your developer email and password and optionally 2FA auth code to login and set the authorization cookie.\n\n> This is a public endpoint and does not require any authentication.\n\nPlease note that this endpoint is not meant for public use and should only be used by the Freemius Developer Dashboard. The login can expect a reCAPTCHA token and it will only work if the reCAPTCHA widget is initialized from the Developer Dashboard itself.\nTo get API tokens for a product or a store, please do it from the Developer Dashboard app itself.\n"
      operationId: developers/log-in
      requestBody:
        content:
          application/json:
            schema:
              properties:
                email:
                  description: 'Valid email address.'
                  type: string
                  example: jane@freemius.com
                  nullable: false
                password:
                  description: 'Valid password.'
                  type: string
                  nullable: false
                recaptcha_token:
                  description: 'reCAPTCHA token. One must use the Developer Dashboard to get the reCAPTCHA token if the login asks for it.'
                  type: string
                remember_me:
                  description: 'Will set the cookie expiration day to 7 days from the successful login if set to `true`. Otherwise, the cookie will expire in 12 hours.'
                  type: boolean
                code:
                  description: '2FA 6 digits code in case developer''s auth mode is using TOTP based 2FA apps.'
                  type: string
                backup_code:
                  description: '2FA backup code (24 chars) to disable and bypass 2FA authentication.'
                  type: string
              type: object
      responses:
        '200':
          description: 'Successful login.'
          content:
            application/json:
              schema:
                properties:
                  person: { $ref: '#/components/schemas/Developer' }
                  expires: { description: 'The expiration time of the cookie in seconds.', type: integer }
                  is_new: { description: 'Signal the developer is not new (this is a login, so it must exists), for consistency with the other auth endpoints.', type: boolean }
                type: object
        '400':
          $ref: '#/components/responses/400'
        '401':
          $ref: '#/components/responses/401'
        '402':
          $ref: '#/components/responses/402'
        '404':
          $ref: '#/components/responses/404'
      security: []
      x-remove-from-doc: true
      x-internal: true
    parameters:
      -
        $ref: '#/components/parameters/developer_id'
  '/products/{product_id}/addons.json':
    get:
      tags:
        - Products
      summary: 'List all addons'
      description: 'Retrieve the addons collection.'
      operationId: products/list-addons
      parameters:
        -
          $ref: '#/components/parameters/count'
        -
          $ref: '#/components/parameters/offset'
        -
          $ref: '#/components/parameters/fields'
        -
          name: show_pending
          in: query
          description: 'Whether to show released addons only or the hidden as well.'
          required: false
          schema:
            type: boolean
            default: false
        -
          name: enriched
          in: query
          description: 'If set to `true`, returns marketing info.'
          required: false
          schema:
            type: boolean
            default: false
      responses:
        '200':
          description: 'The list of all the addons.'
          content:
            application/json:
              schema:
                properties:
                  addons: { type: array, items: { $ref: '#/components/schemas/Plugin' } }
                type: object
        '400':
          $ref: '#/components/responses/400'
        '401':
          $ref: '#/components/responses/401'
        '402':
          $ref: '#/components/responses/402'
        '404':
          $ref: '#/components/responses/404'
    parameters:
      -
        $ref: '#/components/parameters/product_id'
  '/products/{product_id}/addons/{addon_id}/plans/{plan_id}/features.json':
    get:
      tags:
        - Addons
      summary: 'List all plan''s features'
      description: 'Retrieve the plan''s features collection for the addon.'
      operationId: addons/list-plans-features
      parameters:
        -
          $ref: '#/components/parameters/count'
        -
          $ref: '#/components/parameters/offset'
        -
          $ref: '#/components/parameters/fields'
      responses:
        '200':
          description: 'List of all the plan''s features for the addon.'
          content:
            application/json:
              schema:
                properties:
                  features: { type: array, items: { $ref: '#/components/schemas/Feature' } }
                type: object
        '400':
          $ref: '#/components/responses/400'
        '401':
          $ref: '#/components/responses/401'
        '402':
          $ref: '#/components/responses/402'
        '404':
          $ref: '#/components/responses/404'
    parameters:
      -
        $ref: '#/components/parameters/product_id'
      -
        $ref: '#/components/parameters/addon_id'
      -
        $ref: '#/components/parameters/plan_id'
  '/products/{product_id}/addons/{addon_id}/plans.json':
    get:
      tags:
        - Addons
      summary: 'List all plans'
      description: 'Retrieve the plans collection for the addon.'
      operationId: addons/list-plans
      parameters:
        -
          $ref: '#/components/parameters/count'
        -
          $ref: '#/components/parameters/offset'
        -
          $ref: '#/components/parameters/fields'
        -
          name: show_pending
          in: query
          description: 'If set to `true`, retrieves unreleased add-ons as well.'
          required: false
          schema:
            type: boolean
            default: false
        -
          name: type
          in: query
          description: 'Whether to show released addons only or the hidden as well.'
          required: false
          schema:
            default: all
            enum:
              - all
              - visible
      responses:
        '200':
          description: 'The list of all the plans for the addon.'
          content:
            application/json:
              schema:
                properties:
                  plans: { type: array, items: { $ref: '#/components/schemas/Plan' } }
                type: object
        '400':
          $ref: '#/components/responses/400'
        '401':
          $ref: '#/components/responses/401'
        '402':
          $ref: '#/components/responses/402'
        '404':
          $ref: '#/components/responses/404'
    parameters:
      -
        $ref: '#/components/parameters/product_id'
      -
        $ref: '#/components/parameters/addon_id'
  '/products/{product_id}/addons/{addon_id}/plans/{plan_id}/pricing.json':
    get:
      tags:
        - Addons
      summary: 'List all pricings'
      description: 'Retrieve the pricing collection for the addon for specific the plan.'
      operationId: addons/list-pricings
      parameters:
        -
          $ref: '#/components/parameters/count'
        -
          $ref: '#/components/parameters/offset'
        -
          $ref: '#/components/parameters/fields'
        -
          name: currency
          in: query
          schema:
            $ref: '#/components/schemas/CommonEnums/properties/Currency'
      responses:
        '200':
          description: 'The list of all the plans for the addon.'
          content:
            application/json:
              schema:
                properties:
                  plans: { type: array, items: { $ref: '#/components/schemas/Pricing' } }
                type: object
        '400':
          $ref: '#/components/responses/400'
        '401':
          $ref: '#/components/responses/401'
        '402':
          $ref: '#/components/responses/402'
        '404':
          $ref: '#/components/responses/404'
    parameters:
      -
        $ref: '#/components/parameters/product_id'
      -
        $ref: '#/components/parameters/addon_id'
      -
        $ref: '#/components/parameters/plan_id'
  '/products/{product_id}/carts/{cart_id}/events.json':
    get:
      tags:
        - Carts
      summary: 'Retrieve cart events'
      description: 'Get the list of events associated with a cart.'
      operationId: carts/retrieve-events
      parameters:
        -
          $ref: '#/components/parameters/offset'
        -
          $ref: '#/components/parameters/count'
      responses:
        '200':
          description: 'The cart''s events collection.'
          content:
            application/json:
              schema:
                properties:
                  events: { type: array, items: { $ref: '#/components/schemas/EventLog' } }
                type: object
        '400':
          $ref: '#/components/responses/400'
        '401':
          $ref: '#/components/responses/401'
        '402':
          $ref: '#/components/responses/402'
        '404':
          $ref: '#/components/responses/404'
    parameters:
      -
        $ref: '#/components/parameters/product_id'
      -
        $ref: '#/components/parameters/cart_id'
  '/products/{product_id}/carts/{cart_id}.json':
    get:
      tags:
        - Carts
      summary: 'Retrieve a cart'
      description: "Retrieve cart details associated with the product.\n\n> You can use `enriched=true` to get more details about the cart, for example the `gross`, `coupon_code` and `licenses` fields will only be returned if enriched is enabled. Please see individual parameters in the response data below to learn more."
      operationId: carts/retrieve
      parameters:
        -
          $ref: '#/components/parameters/fields'
        -
          name: enriched
          in: query
          description: 'Defaults to false, if true returns enriched cart details.'
          schema:
            type: boolean
            default: 'false'
      responses:
        '200':
          description: 'Cart details associated with the product.'
          content:
            application/json:
              schema:
                allOf:
                  - { $ref: '#/components/schemas/Cart' }
                  - { properties: { gross: { description: 'Gross amount associated with the cart. (Only available when `enriched` is set to `true`.)', type: number, format: float, example: '359.64', nullable: true }, coupon_code: { description: 'Coupon code associated with the cart. (Only available when `enriched` is set to `true`.)', type: string, example: BLACKFRIDAY2024, nullable: true }, licenses: { description: 'Number of licenses associated with the cart. (Only available when `enriched` is set to `true`.)', type: number, example: '10', nullable: true } }, type: object }
        '400':
          $ref: '#/components/responses/400'
        '401':
          $ref: '#/components/responses/401'
        '402':
          $ref: '#/components/responses/402'
    put:
      tags:
        - Carts
      summary: 'Update a cart'
      description: "Update the details of a particular cart.\n\n> Updating a completed checkout cart is prohibited.\n\n> Updating the coupon requires both the `coupon_id` and `coupon_code`."
      operationId: carts/update
      parameters:
        -
          $ref: '#/components/parameters/fields'
      requestBody:
        required: true
        content:
          application/json:
            schema:
              description: 'All these fields are optional. Note: You can update any of the fields. If you don''t provide a field, it will remain unchanged.'
              properties:
                plan_id:
                  description: 'The Plan ID.'
                  type: number
                  example: '1234'
                pricing_id:
                  $ref: '#/components/schemas/CommonProperties/properties/pricing_id'
                payment_method:
                  $ref: '#/components/schemas/CommonEnums/properties/PaymentMethodType'
                billing_cycle:
                  $ref: '#/components/schemas/CommonEnums/properties/BillingCycle'
                coupon_id:
                  $ref: '#/components/schemas/CommonProperties/properties/coupon_id'
                coupon_code:
                  $ref: '#/components/schemas/CommonProperties/properties/coupon_code'
                country_code:
                  $ref: '#/components/schemas/CommonProperties/properties/country_code_nullable'
                vat_id:
                  $ref: '#/components/schemas/CommonProperties/properties/vat_id_nullable'
                email:
                  $ref: '#/components/schemas/Cart/properties/email'
                first:
                  $ref: '#/components/schemas/Cart/properties/first'
                last:
                  $ref: '#/components/schemas/Cart/properties/last'
                ip:
                  $ref: '#/components/schemas/CommonProperties/properties/ip'
              type: object
      responses:
        '200':
          description: 'Provides the updated cart with details.'
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Cart'
        '400':
          $ref: '#/components/responses/400'
        '401':
          $ref: '#/components/responses/401'
        '402':
          $ref: '#/components/responses/402'
      x-remove-from-doc: true
      x-internal: true
    delete:
      tags:
        - Carts
      summary: 'Delete a cart'
      description: 'Delete a particular cart.'
      operationId: carts/delete
      responses:
        '204':
          $ref: '#/components/responses/204'
        '400':
          $ref: '#/components/responses/400'
        '401':
          $ref: '#/components/responses/401'
        '402':
          $ref: '#/components/responses/402'
      x-remove-from-doc: true
      x-internal: true
    parameters:
      -
        $ref: '#/components/parameters/product_id'
      -
        $ref: '#/components/parameters/cart_id'
  '/products/{product_id}/carts.json':
    get:
      tags:
        - Carts
      summary: 'List all carts'
      description: "Retrieve the cart collection associated with your product.\n\n> If `enriched=true` you will get more details about the cart for example the `gross`, `coupon_code` and `licenses` fields.\n\n> You can use the `filter` or `email` or `count` parameters to get more refined results from your query. Please learn more about the individual parameters below."
      operationId: carts/list
      parameters:
        -
          name: filter
          in: query
          description: 'You can use the `filter` parameter to filter by status. If you don''t provide a status, the endpoint will return all carts.'
          schema:
            type: string
            default: all
            enum:
              - all
              - abandoned
              - completed
              - recovered
              - recovery
              - active
        -
          $ref: '#/components/parameters/offset'
        -
          $ref: '#/components/parameters/fields'
        -
          name: enriched
          in: query
          description: 'Defaults to false, if true returns enriched cart details.'
          schema:
            type: boolean
            default: 'false'
        -
          name: email
          in: query
          description: 'Filter the cart collections by the email address.'
          schema:
            type: string
            example: doe@example.com
        -
          name: count
          in: query
          description: 'Number of carts to retrieve.'
          schema:
            type: integer
            default: '50'
      responses:
        '200':
          description: 'Provides a collection of carts associated with the product. All carts are listed under the `carts` key.'
          content:
            application/json:
              schema:
                properties:
                  carts: { type: array, items: { allOf: [{ $ref: '#/components/schemas/Cart' }, { properties: { gross: { description: 'Email of the user associated with the cart. (Only available when `enriched` is set to `true`.)', type: number, format: float, example: '359.64', nullable: true }, coupon_code: { description: 'Coupon code associated with the cart. (Only available when `enriched` is set to `true`.)', type: string, example: BLACKFRIDAY2024, nullable: true }, licenses: { description: 'Number of licenses associated with the cart. (Only available when `enriched` is set to `true`.)', type: number, example: '10', nullable: true } }, type: object }] } }
                type: object
        '400':
          $ref: '#/components/responses/400'
        '401':
          $ref: '#/components/responses/401'
        '402':
          $ref: '#/components/responses/402'
    parameters:
      -
        $ref: '#/components/parameters/product_id'
  '/products/{product_id}/coupons/{coupon_id}.json':
    get:
      tags:
        - Coupons
      summary: 'Retrieve a coupon'
      description: 'Get details of a specific coupon by ID.'
      operationId: coupons/retrieve
      responses:
        '200':
          description: 'The coupon is retrieved successfully.'
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Coupon'
        '400':
          $ref: '#/components/responses/400'
        '401':
          $ref: '#/components/responses/401'
        '402':
          $ref: '#/components/responses/402'
        '404':
          $ref: '#/components/responses/404'
    put:
      tags:
        - Coupons
      summary: 'Update a coupon'
      description: 'Update a specific coupon''s details by ID.'
      operationId: coupons/update
      requestBody:
        required: true
        content:
          application/json:
            schema:
              properties:
                plans:
                  $ref: '#/components/schemas/Coupon/properties/plans'
                licenses:
                  $ref: '#/components/schemas/Coupon/properties/licenses'
                billing_cycles:
                  $ref: '#/components/schemas/Coupon/properties/billing_cycles'
                user_type:
                  $ref: '#/components/schemas/Coupon/properties/user_type'
                code:
                  $ref: '#/components/schemas/Coupon/properties/code'
                discount:
                  $ref: '#/components/schemas/Coupon/properties/discount'
                discount_type:
                  $ref: '#/components/schemas/Coupon/properties/discount_type'
                start_date:
                  $ref: '#/components/schemas/Coupon/properties/start_date'
                end_date:
                  $ref: '#/components/schemas/Coupon/properties/end_date'
                redemptions_limit:
                  $ref: '#/components/schemas/Coupon/properties/redemptions_limit'
                has_renewals_discount:
                  $ref: '#/components/schemas/Coupon/properties/has_renewals_discount'
                has_addons_discount:
                  $ref: '#/components/schemas/Coupon/properties/has_addons_discount'
                is_one_per_user:
                  $ref: '#/components/schemas/Coupon/properties/is_one_per_user'
                is_active:
                  $ref: '#/components/schemas/Coupon/properties/is_active'
              type: object
      responses:
        '200':
          description: 'The coupon is updated.'
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Coupon'
        '400':
          $ref: '#/components/responses/400'
        '401':
          $ref: '#/components/responses/401'
        '402':
          $ref: '#/components/responses/402'
        '404':
          $ref: '#/components/responses/404'
    delete:
      tags:
        - Coupons
      summary: 'Delete a coupon'
      description: 'Delete a specific coupon by ID.'
      operationId: coupons/delete
      responses:
        '204':
          $ref: '#/components/responses/204'
        '400':
          $ref: '#/components/responses/400'
        '401':
          $ref: '#/components/responses/401'
        '402':
          $ref: '#/components/responses/402'
        '404':
          $ref: '#/components/responses/404'
    parameters:
      -
        $ref: '#/components/parameters/product_id'
      -
        $ref: '#/components/parameters/coupon_id'
  '/products/{product_id}/coupons.json':
    get:
      tags:
        - Coupons
      summary: 'List all coupons'
      description: "Retrieve the coupon collection associated with your product.\n\n### Searching and filtering\n\nYou can use filtering to search for a particular coupon or a group of coupons. The available parameters are:\n\n- `code` - You can explicitly search coupon by the code.\n- `search` - You can search by coupon code or coupon ID.\n- `prefix` - You can filter by coupon code prefix.\n\n> If using search and filtering, then the `is_enriched` parameter is ignored.\n"
      operationId: coupons/list
      parameters:
        -
          name: code
          in: query
          description: 'The coupon code filter.'
          required: false
          schema:
            type: string
        -
          name: is_enriched
          in: query
          description: 'If `true`, each coupon will include multi-currency discount properties. Coupons will only be enriched if no filtering is used.'
          schema:
            type: boolean
        -
          $ref: '#/components/parameters/count'
        -
          $ref: '#/components/parameters/offset'
        -
          name: prefix
          in: query
          description: 'Optional coupon code prefix for search coupons.'
          schema:
            type: string
        -
          name: search
          in: query
          description: 'Optional coupon code(or code part) for search coupons.'
          schema:
            type: string
      responses:
        '200':
          description: 'Provides a collection of coupons associated with the product. All coupons are listed under the `coupons` key.'
          content:
            application/json:
              schema:
                properties:
                  coupons: { type: array, items: { allOf: [{ $ref: '#/components/schemas/Coupon' }, { properties: { discounts: { type: object } }, type: object }] } }
                type: object
        '400':
          $ref: '#/components/responses/400'
        '401':
          $ref: '#/components/responses/401'
        '402':
          $ref: '#/components/responses/402'
    post:
      tags:
        - Coupons
      summary: 'Create a coupon'
      description: "Create a new coupon.\n\nAlternatively, you can use the [Freemius Developer Dashboard](https://dashboard.freemius.com).\n\n> If you're creating coupon from your SaaS for some specific use case, please be sure to set the `plans`, `redemptions_limit`, `end_date`, and `is_one_per_user` properties to the appropriate values, to avoid misuse."
      operationId: coupons/create
      requestBody:
        required: true
        content:
          application/json:
            schema:
              properties:
                plans:
                  $ref: '#/components/schemas/Coupon/properties/plans'
                licenses:
                  $ref: '#/components/schemas/Coupon/properties/licenses'
                billing_cycles:
                  $ref: '#/components/schemas/Coupon/properties/billing_cycles'
                user_type:
                  $ref: '#/components/schemas/Coupon/properties/user_type'
                code:
                  $ref: '#/components/schemas/Coupon/properties/code'
                discount:
                  $ref: '#/components/schemas/Coupon/properties/discount'
                discount_type:
                  $ref: '#/components/schemas/Coupon/properties/discount_type'
                start_date:
                  $ref: '#/components/schemas/Coupon/properties/start_date'
                end_date:
                  $ref: '#/components/schemas/Coupon/properties/end_date'
                redemptions_limit:
                  $ref: '#/components/schemas/Coupon/properties/redemptions_limit'
                has_renewals_discount:
                  $ref: '#/components/schemas/Coupon/properties/has_renewals_discount'
                has_addons_discount:
                  $ref: '#/components/schemas/Coupon/properties/has_addons_discount'
                is_one_per_user:
                  $ref: '#/components/schemas/Coupon/properties/is_one_per_user'
                is_active:
                  $ref: '#/components/schemas/Coupon/properties/is_active'
              type: object
      responses:
        '201':
          description: 'The coupon is created.'
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Coupon'
        '400':
          $ref: '#/components/responses/400'
        '401':
          $ref: '#/components/responses/401'
        '402':
          $ref: '#/components/responses/402'
    parameters:
      -
        $ref: '#/components/parameters/product_id'
  '/products/{product_id}/coupons/{coupon_id}/note.json':
    get:
      tags:
        - Coupons
      summary: 'Retrieve a note'
      description: 'Get the details of a note associated with a coupon.'
      operationId: coupons/retrieve-note
      responses:
        '200':
          description: 'The coupon note details.'
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Note'
        '400':
          $ref: '#/components/responses/400'
        '401':
          $ref: '#/components/responses/401'
        '402':
          $ref: '#/components/responses/402'
        '404':
          $ref: '#/components/responses/404'
    put:
      tags:
        - Coupons
      summary: 'Update a note'
      description: 'Update a note for a coupon.'
      operationId: coupons/update-note
      requestBody:
        content:
          application/json:
            schema:
              properties:
                note:
                  type: string
                  example: 'This is an updated note.'
              type: object
      responses:
        '200':
          description: 'The coupon note was updated.'
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Note'
        '400':
          $ref: '#/components/responses/400'
        '401':
          $ref: '#/components/responses/401'
        '402':
          $ref: '#/components/responses/402'
        '404':
          $ref: '#/components/responses/404'
    post:
      tags:
        - Coupons
      summary: 'Create a note'
      description: 'Create a new note for a coupon.'
      operationId: coupons/create-note
      requestBody:
        content:
          application/json:
            schema:
              properties:
                note:
                  type: string
                  example: 'This is a note.'
              type: object
      responses:
        '201':
          description: 'The note was added to the coupon.'
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Note'
        '400':
          $ref: '#/components/responses/400'
        '401':
          $ref: '#/components/responses/401'
        '402':
          $ref: '#/components/responses/402'
        '404':
          $ref: '#/components/responses/404'
    delete:
      tags:
        - Coupons
      summary: 'Delete a note'
      description: 'Delete a note for a coupon.'
      operationId: coupons/delete-note
      responses:
        '204':
          $ref: '#/components/responses/204'
        '400':
          $ref: '#/components/responses/400'
        '401':
          $ref: '#/components/responses/401'
        '402':
          $ref: '#/components/responses/402'
        '404':
          $ref: '#/components/responses/404'
    parameters:
      -
        $ref: '#/components/parameters/product_id'
      -
        $ref: '#/components/parameters/coupon_id'
  '/products/{product_id}/coupons/special.json':
    get:
      tags:
        - Coupons
      summary: 'Retrieve special coupons'
      description: "Get the details of a special coupon.\n     *\n### Searching and filtering\n\nYou can use filtering to search for a particular coupon or a group of coupons by `type`."
      operationId: coupons/retrieve-special
      parameters:
        -
          name: type
          in: query
          description: 'Filter based on a coupon type.'
          required: false
          schema:
            $ref: '#/components/schemas/CouponEntity/properties/type'
      responses:
        '200':
          description: 'The special coupons details.'
          content:
            application/json:
              schema:
                properties:
                  coupon_entities: { type: array, items: { $ref: '#/components/schemas/CouponEntityEnriched' } }
                type: object
        '400':
          $ref: '#/components/responses/400'
        '401':
          $ref: '#/components/responses/401'
        '402':
          $ref: '#/components/responses/402'
        '404':
          $ref: '#/components/responses/404'
    parameters:
      -
        $ref: '#/components/parameters/product_id'
  '/products/{product_id}/coupons/{coupon_id}/special/{special_id}.json':
    put:
      tags:
        - Coupons
      summary: 'Create a special coupon'
      description: 'Create a special coupon.'
      operationId: coupons/create-special
      responses:
        '201':
          description: 'The special coupon has been created.'
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/CouponEntityEnriched'
        '400':
          $ref: '#/components/responses/400'
        '401':
          $ref: '#/components/responses/401'
        '402':
          $ref: '#/components/responses/402'
        '404':
          $ref: '#/components/responses/404'
    delete:
      tags:
        - Coupons
      summary: 'Delete a special coupon'
      description: 'Delete a special coupon by ID.'
      operationId: coupons/delete-special
      responses:
        '204':
          $ref: '#/components/responses/204'
        '400':
          $ref: '#/components/responses/400'
        '401':
          $ref: '#/components/responses/401'
        '402':
          $ref: '#/components/responses/402'
        '404':
          $ref: '#/components/responses/404'
    parameters:
      -
        $ref: '#/components/parameters/product_id'
      -
        $ref: '#/components/parameters/coupon_id'
      -
        $ref: '#/components/parameters/special_id'
  '/products/{product_id}/emails/addresses.json':
    get:
      tags:
        - Products
      summary: 'List all email addresses'
      description: 'Retrieve the email addresses collection associated with a product. In case the product is using the store''s email address configuration, the endpoint will return a `404` error.'
      operationId: products/list-email-addresses
      parameters:
        -
          $ref: '#/components/parameters/fields'
      responses:
        '200':
          description: 'The list of all the email addresses associated with a product.'
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/PluginEmailAddress'
        '400':
          $ref: '#/components/responses/400'
        '401':
          $ref: '#/components/responses/401'
        '402':
          $ref: '#/components/responses/402'
        '404':
          $ref: '#/components/responses/404'
    delete:
      tags:
        - Products
      summary: 'Delete all email addresses'
      description: 'Delete all email addresses associated with a product. Sets the product to use the default store-level email addresses.'
      operationId: products/delete-email-addresses
      responses:
        '204':
          description: 'Email addresses deleted. Product set to use the default store-level email addresses.'
        '400':
          $ref: '#/components/responses/400'
        '401':
          $ref: '#/components/responses/401'
        '402':
          $ref: '#/components/responses/402'
        '404':
          $ref: '#/components/responses/404'
    parameters:
      -
        $ref: '#/components/parameters/product_id'
  '/developers/{developer_id}/products/{product_id}/emails/addresses.json':
    put:
      tags:
        - Products
      summary: 'Update email addressses'
      description: "Update the email addresses associated with a product.\n\n> Only a plugin's developer can update the email addresses of their plugin."
      operationId: products/update-email-addressses
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/PluginEmailAddress'
      responses:
        '204':
          description: 'Email addresses updated.'
        '400':
          $ref: '#/components/responses/400'
        '401':
          $ref: '#/components/responses/401'
        '402':
          $ref: '#/components/responses/402'
        '404':
          $ref: '#/components/responses/404'
      security:
        -
          ApiAuthFSACookie: []
        -
          ApiAuthFSAHeader: []
      x-remove-from-doc: true
      x-internal: true
    parameters:
      -
        $ref: '#/components/parameters/developer_id'
      -
        $ref: '#/components/parameters/product_id'
  '/products/{product_id}/events/{event_id}.json':
    get:
      tags:
        - Events
      summary: 'Retrieve an event'
      description: 'Retrieve a specific event by its ID. For instructions on creating webhook listeners, see the [documentation](help-documentation-saas-events-webhooks.md#how_to_create_a_webhook).'
      operationId: events/retrieve
      parameters:
        -
          $ref: '#/components/parameters/fields'
      responses:
        '200':
          description: 'The retrieved event.'
          content:
            application/json:
              schema:
                allOf:
                  - { $ref: '#/components/schemas/EventLog' }
                  - { properties: { objects: { description: 'A map of related objects keyed by their type or ID, such as Payment, User, Install, or License.', properties: { user: { oneOf: [{ $ref: '#/components/schemas/UserPluginEnriched' }], nullable: true }, install: { oneOf: [{ $ref: '#/components/schemas/Install' }], nullable: true }, payment: { oneOf: [{ $ref: '#/components/schemas/Payment' }], nullable: true }, subscription: { oneOf: [{ $ref: '#/components/schemas/Subscription' }], nullable: true }, license: { oneOf: [{ $ref: '#/components/schemas/License' }], nullable: true } }, type: object, additionalProperties: true } }, type: object, example: { objects: { user: { id: '1234567', email: user@example.com, first: Joe, last: Doe, is_verified: true }, install: { id: '1234567', plugin_id: '12345', user_id: '1234567', url: 'https://example.com', plan_id: '12345' }, license: { plugin_id: '12345', user_id: '12345', plan_id: '12345', pricing_id: '12345', quota: 10, expiration: '2025-10-01 10:11:46', id: '1234567', created: '2025-01-01 01:11:46', updated: '2025-01-01 01:11:46' }, payment: { subscription_id: '12345', gross: 14.99, gateway_fee: 0.41, vat: 1.52, is_renewal: true, type: payment, user_id: '12345', install_id: '12345', plan_id: '12345', pricing_id: '12345', license_id: '12345' } } } }
        '400':
          $ref: '#/components/responses/400'
        '401':
          $ref: '#/components/responses/401'
        '402':
          $ref: '#/components/responses/402'
        '404':
          $ref: '#/components/responses/404'
    parameters:
      -
        $ref: '#/components/parameters/product_id'
      -
        $ref: '#/components/parameters/event_id'
  '/products/{product_id}/events.json':
    get:
      tags:
        - Events
      summary: 'List all events'
      description: 'Retrieve a list of events for a specific product. Supports filtering by type, state, and pagination. See the [documentation](help-documentation-saas-events-webhooks.md#how_to_create_a_webhook) for instructions on creating a webhook to listen for events.'
      operationId: events/list
      parameters:
        -
          name: type
          in: query
          description: 'Filter events by type string or event name, such as `license.created`. See the [documentation](help-documentation-saas-events-webhooks.md#event_types) for a list of available event types.'
          required: false
          schema:
            type: string
        -
          name: state
          in: query
          description: 'Filter events by state: ''pending'', ''processed'', ''error'', or ''canceled''.'
          required: false
          schema:
            $ref: '#/components/schemas/CommonEnums/properties/EventLogState'
        -
          $ref: '#/components/parameters/count'
        -
          $ref: '#/components/parameters/offset'
        -
          $ref: '#/components/parameters/fields'
      responses:
        '200':
          description: 'A collection of events.'
          content:
            application/json:
              schema:
                properties:
                  events: { type: array, items: { $ref: '#/components/schemas/EventLog' } }
                type: object
        '400':
          $ref: '#/components/responses/400'
        '401':
          $ref: '#/components/responses/401'
        '402':
          $ref: '#/components/responses/402'
        '404':
          $ref: '#/components/responses/404'
    parameters:
      -
        $ref: '#/components/parameters/product_id'
  '/products/{product_id}/features/{feature_id}.json':
    get:
      tags:
        - Products
      summary: 'Retrieve a feature'
      description: 'Retrieve a product''s feature.'
      operationId: products/retrieve-feature
      parameters:
        -
          $ref: '#/components/parameters/fields'
      responses:
        '200':
          description: 'The product''s feature.'
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Feature'
        '400':
          $ref: '#/components/responses/400'
        '401':
          $ref: '#/components/responses/401'
        '402':
          $ref: '#/components/responses/402'
        '404':
          $ref: '#/components/responses/404'
    put:
      tags:
        - Products
      summary: 'Update a feature'
      description: 'Update a product''s feature. Please note that the `value` attribute can only be set and updated per plan with a developer scope authorization.'
      operationId: products/update-feature
      requestBody:
        required: false
        content:
          application/json:
            schema:
              properties:
                title:
                  $ref: '#/components/schemas/Feature/properties/title'
                description:
                  $ref: '#/components/schemas/Feature/properties/description'
                is_featured:
                  $ref: '#/components/schemas/Feature/properties/is_featured'
              type: object
      responses:
        '200':
          description: 'The updated feature.'
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Feature'
        '400':
          $ref: '#/components/responses/400'
        '401':
          $ref: '#/components/responses/401'
        '402':
          $ref: '#/components/responses/402'
        '404':
          $ref: '#/components/responses/404'
    delete:
      tags:
        - Products
      summary: 'Delete a feature'
      description: 'Delete a product''s feature.'
      operationId: products/delete-feature
      responses:
        '204':
          $ref: '#/components/responses/204'
        '400':
          $ref: '#/components/responses/400'
        '401':
          $ref: '#/components/responses/401'
        '402':
          $ref: '#/components/responses/402'
        '404':
          $ref: '#/components/responses/404'
    parameters:
      -
        $ref: '#/components/parameters/product_id'
      -
        $ref: '#/components/parameters/feature_id'
  '/products/{product_id}/features.json':
    get:
      tags:
        - Products
      summary: 'List all features'
      description: 'Retrieve the product features collection.'
      operationId: products/list-features
      parameters:
        -
          $ref: '#/components/parameters/count'
        -
          $ref: '#/components/parameters/offset'
        -
          $ref: '#/components/parameters/fields'
      responses:
        '200':
          description: 'The product features collection.'
          content:
            application/json:
              schema:
                properties:
                  features: { type: array, items: { allOf: [{ $ref: '#/components/schemas/Feature' }] } }
                type: object
        '400':
          $ref: '#/components/responses/400'
        '401':
          $ref: '#/components/responses/401'
        '402':
          $ref: '#/components/responses/402'
        '404':
          $ref: '#/components/responses/404'
    parameters:
      -
        $ref: '#/components/parameters/product_id'
  '/products/{product_id}.json':
    get:
      tags:
        - Products
      summary: 'Retrieve a product'
      description: 'Query and retrieve a specific product by ID.'
      operationId: products/retrieve
      parameters:
        -
          $ref: '#/components/parameters/fields'
        -
          parameter: is_enriched
          name: is_enriched
          in: query
          description: 'Whether to return an enriched product response with additional properties relevant for the frontend.'
          schema:
            type: boolean
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Plugin'
        '400':
          $ref: '#/components/responses/400'
        '401':
          $ref: '#/components/responses/401'
        '402':
          $ref: '#/components/responses/402'
        '404':
          $ref: '#/components/responses/404'
    put:
      tags:
        - Products
      summary: 'Update a product'
      description: 'Update a specific product by ID.'
      operationId: products/update
      requestBody:
        content:
          multipart/form-data:
            schema:
              properties:
                icon:
                  $ref: '#/components/schemas/CommonProperties/properties/icon'
                data:
                  $ref: '#/components/schemas/CommonRequestSchemas/properties/MultipartJsonData'
              type: object
          application/json:
            schema:
              description: 'Data needed to create or update a product'
              properties:
                slug:
                  $ref: '#/components/schemas/Plugin/properties/slug'
                title:
                  $ref: '#/components/schemas/Plugin/properties/title'
                type:
                  $ref: '#/components/schemas/Plugin/properties/type'
                plans:
                  $ref: '#/components/schemas/Plugin/properties/plans'
                features:
                  $ref: '#/components/schemas/Plugin/properties/features'
                money_back_period:
                  $ref: '#/components/schemas/Plugin/properties/money_back_period'
                refund_policy:
                  $ref: '#/components/schemas/Plugin/properties/refund_policy'
                annual_renewals_discount:
                  $ref: '#/components/schemas/Plugin/properties/annual_renewals_discount'
                renewals_discount_type:
                  $ref: '#/components/schemas/Plugin/properties/renewals_discount_type'
                lifetime_license_proration_days:
                  $ref: '#/components/schemas/Plugin/properties/lifetime_license_proration_days'
                is_pricing_visible:
                  $ref: '#/components/schemas/Plugin/properties/is_pricing_visible'
                default_plan_id:
                  $ref: '#/components/schemas/Plugin/properties/default_plan_id'
                accepted_payments:
                  description: 'Can be one of the following values: `1` for `PayPal`, `2` for `Credit Cards`, or `0` for both.'
                  type: integer
                  enum: [0, 1]
                expose_license_key:
                  description: '`True` to expose license key to customers upon purchase/subscription. (Available for ''SaaS'' products only)'
                  type: boolean
                enable_after_purchase_email_login_link:
                  description: '`True` to include in the after-purchase emails the customer portal login link.'
                  type: boolean
              type: object
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Plugin'
        '400':
          $ref: '#/components/responses/400'
        '401':
          $ref: '#/components/responses/401'
        '402':
          $ref: '#/components/responses/402'
        '404':
          $ref: '#/components/responses/404'
    parameters:
      -
        $ref: '#/components/parameters/product_id'
  '/products/{product_id}/info.json':
    get:
      tags:
        - Products
      summary: 'Get product info'
      description: 'Get product info. Please use the Developer Dashboard to update the information of a product.'
      operationId: products/get-info
      parameters:
        -
          $ref: '#/components/parameters/fields'
      responses:
        '200':
          description: 'Successful operation'
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/PluginInfo'
        '400':
          $ref: '#/components/responses/400'
        '401':
          $ref: '#/components/responses/401'
        '402':
          $ref: '#/components/responses/402'
        '404':
          $ref: '#/components/responses/404'
    parameters:
      -
        $ref: '#/components/parameters/product_id'
  '/products/{product_id}/installs/{install_id}/addons/{addon_id}/plans/{plan_id}/features.json':
    get:
      tags:
        - Installations
      summary: 'List all plan''s features for Addon'
      description: 'Get plan''s features collection for an addon on a site.'
      operationId: installations/list-plans-features-for-addon
      parameters:
        -
          $ref: '#/components/parameters/count'
        -
          $ref: '#/components/parameters/offset'
        -
          $ref: '#/components/parameters/fields'
      responses:
        '200':
          description: 'The plan''s features collection for Addon on an install.'
          content:
            application/json:
              schema:
                properties:
                  features: { type: array, items: { $ref: '#/components/schemas/Feature' } }
                type: object
        '400':
          $ref: '#/components/responses/400'
        '401':
          $ref: '#/components/responses/401'
        '402':
          $ref: '#/components/responses/402'
        '404':
          $ref: '#/components/responses/404'
    parameters:
      -
        $ref: '#/components/parameters/product_id'
      -
        $ref: '#/components/parameters/install_id'
      -
        $ref: '#/components/parameters/addon_id'
      -
        $ref: '#/components/parameters/plan_id'
  '/products/{product_id}/installs/{install_id}/clones/{clone_id}.json':
    put:
      tags:
        - Installations
      summary: 'Resolve a clone'
      description: 'Resolve a clone of an install that was created by the product.'
      operationId: installations/resolve-clone
      parameters:
        -
          $ref: '#/components/parameters/fields'
      requestBody:
        required: true
        content:
          application/json:
            schema:
              required:
                - resolution
              properties:
                resolution:
                  $ref: '#/components/schemas/InstallClone/properties/resolution'
                new_install_id:
                  $ref: '#/components/schemas/InstallClone/properties/new_install_id'
              type: object
      responses:
        '200':
          description: 'Install clone created.'
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/InstallClone'
        '400':
          $ref: '#/components/responses/400'
        '401':
          $ref: '#/components/responses/401'
        '404':
          $ref: '#/components/responses/404'
      x-remove-from-doc: true
      x-internal: true
    parameters:
      -
        $ref: '#/components/parameters/product_id'
      -
        $ref: '#/components/parameters/install_id'
      -
        $ref: '#/components/parameters/clone_id'
  '/products/{product_id}/installs/{install_id}/clones.json':
    post:
      tags:
        - Installations
      summary: 'Create a clone'
      description: "Create a clone of an install associated with the product.\n\n> Use this endpoint if you want to support migration or temporary or long-term duplicates for staging purposes.\n\nBy default the clone will be created in a pending state. For our [WP SDK](help-documentation-wordpress-sdk-safe-mode-clone-resolution-duplicate-website.md) the clone will be created in a safe mode state.\n\nAfter creating the clone, you will need to resolve the clone by updating its state and resolution. You will need to handle the licensing logic for the new install entity. Our [WP SDK](help-documentation-wordpress-sdk-safe-mode-clone-resolution-duplicate-website.md) handles it automatically for WordPress products (plugins and themes)."
      operationId: installations/create-clone
      parameters:
        -
          $ref: '#/components/parameters/fields'
      requestBody:
        content:
          application/json:
            schema:
              required:
                - site_url
              properties:
                site_url:
                  description: 'The URL of the new site to clone the install to.'
                  type: string
                  example: 'https://example.com'
              type: object
      responses:
        '200':
          description: 'Install clone created.'
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/InstallClone'
        '400':
          $ref: '#/components/responses/400'
        '401':
          $ref: '#/components/responses/401'
        '404':
          $ref: '#/components/responses/404'
      x-remove-from-doc: true
      x-internal: true
    parameters:
      -
        $ref: '#/components/parameters/product_id'
      -
        $ref: '#/components/parameters/install_id'
  '/products/{product_id}/installs/count.json':
    get:
      tags:
        - Installations
      summary: 'Retrieve installs count'
      description: "Retrieve the number of installs associated with the product.\n\n### Filtering\n\nYou can filter the count by `plan_id` or `is_active`."
      operationId: installations/retrieve-installs-count
      parameters:
        -
          name: plan_id
          in: query
          description: '(optional) Return the count of installs that are associated with a non-expired license for the given plan ID.'
          schema:
            type: number
            example: 1
        -
          name: is_active
          in: query
          description: '(optional) Return active installs only.'
          schema:
            type: boolean
            example: false
      responses:
        '200':
          description: 'The number of installs with the product.'
          content:
            application/json:
              schema:
                properties:
                  count: { type: integer, minimum: 0, example: 123 }
                type: object
    parameters:
      -
        $ref: '#/components/parameters/product_id'
  '/products/{product_id}/installs/{install_id}/downgrade.json':
    put:
      tags:
        - Installations
      summary: 'Downgrade to the default plan'
      description: 'Downgrade install''s plan to product’s default plan. This is usually the free plan.'
      operationId: installations/downgrade-default-plan
      parameters:
        -
          $ref: '#/components/parameters/fields'
      requestBody:
        required: true
        content:
          application/json:
            schema:
              properties:
                deactivate_license:
                  description: 'Deactivate license.'
                  type: boolean
                reason_ids:
                  $ref: '#/components/schemas/Uninstall/properties/reason_id'
                reason:
                  $ref: '#/components/schemas/Uninstall/properties/reason_info'
              type: object
      responses:
        '200':
          description: 'Product plan downgraded.'
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Install'
        '400':
          $ref: '#/components/responses/400'
        '401':
          $ref: '#/components/responses/401'
        '402':
          $ref: '#/components/responses/402'
        '404':
          $ref: '#/components/responses/404'
    parameters:
      -
        $ref: '#/components/parameters/product_id'
      -
        $ref: '#/components/parameters/install_id'
  '/products/{product_id}/installs/{install_id}/events.json':
    get:
      tags:
        - Installations
      summary: 'List all events'
      description: 'Retrieve the event collection related to a product install.'
      operationId: installations/list-events
      parameters:
        -
          $ref: '#/components/parameters/count'
        -
          $ref: '#/components/parameters/offset'
        -
          $ref: '#/components/parameters/fields'
        -
          name: type
          in: query
          description: 'Filter events by type string or event name.'
          schema:
            type: string
            example: license.activated
      responses:
        '200':
          description: 'Events triggered by the install.'
          content:
            application/json:
              schema:
                properties:
                  events: { type: array, items: { $ref: '#/components/schemas/EventLog' } }
                type: object
        '400':
          $ref: '#/components/responses/400'
        '401':
          $ref: '#/components/responses/401'
        '402':
          $ref: '#/components/responses/402'
        '404':
          $ref: '#/components/responses/404'
    parameters:
      -
        $ref: '#/components/parameters/product_id'
      -
        $ref: '#/components/parameters/install_id'
  '/products/{product_id}/installs/{install_id}.json':
    get:
      tags:
        - Installations
      summary: 'Retrieve an install'
      description: 'Retrieve the details related to the product install.'
      operationId: installations/retrieve-install
      parameters:
        -
          $ref: '#/components/parameters/fields'
      responses:
        '200':
          description: 'The install details.'
          content:
            application/json:
              schema:
                allOf:
                  - { $ref: '#/components/schemas/Install' }
                  - { properties: { is_beta: { description: 'Whether the install is participating in the beta program.', type: boolean } }, type: object }
        '400':
          $ref: '#/components/responses/400'
        '401':
          $ref: '#/components/responses/401'
        '404':
          $ref: '#/components/responses/404'
    put:
      tags:
        - Installations
      summary: 'Update an install'
      description: 'Update the details related to the product install.'
      operationId: installations/update-install
      requestBody:
        required: true
        content:
          application/json:
            schema:
              properties:
                uid:
                  $ref: '#/components/schemas/CommonProperties/properties/uid'
                license_key:
                  $ref: '#/components/schemas/License/properties/secret_key'
                url:
                  $ref: '#/components/schemas/Install/properties/url'
                title:
                  $ref: '#/components/schemas/Install/properties/title'
                version:
                  $ref: '#/components/schemas/Install/properties/version'
                sdk_version:
                  $ref: '#/components/schemas/Install/properties/sdk_version'
                platform_version:
                  $ref: '#/components/schemas/Install/properties/platform_version'
                programming_language_version:
                  $ref: '#/components/schemas/Install/properties/programming_language_version'
                plan_id:
                  $ref: '#/components/schemas/Plan/properties/id'
                trial_plan_id:
                  $ref: '#/components/schemas/Install/properties/trial_plan_id'
                trials_ends:
                  description: 'The datetime that the trial expires.'
                  type: string
                  format: date-time
                  example: '2025-01-01 00:00:00'
                subscription_id:
                  $ref: '#/components/schemas/Subscription/properties/id'
                is_locked:
                  $ref: '#/components/schemas/Install/properties/is_locked'
                is_active:
                  $ref: '#/components/schemas/Install/properties/is_active'
                is_disconnected:
                  $ref: '#/components/schemas/Install/properties/is_disconnected'
                is_premium:
                  $ref: '#/components/schemas/Install/properties/is_premium'
                is_sdk_required:
                  $ref: '#/components/schemas/Plugin/properties/is_sdk_required'
                reason_id:
                  $ref: '#/components/schemas/Uninstall/properties/reason_id'
                reason_info:
                  $ref: '#/components/schemas/Uninstall/properties/reason_info'
                plugins:
                  description: 'The site plugins installed.'
                  type: string
                themes:
                  description: 'The site themes installed.'
                  type: string
                is_beta:
                  $ref: '#/components/schemas/BetaParticipation/properties/is_beta'
                recover:
                  description: 'Recover the install.'
                  type: boolean
                is_uninstalled:
                  $ref: '#/components/schemas/Install/properties/is_uninstalled'
                user_id:
                  description: 'The ID of the user. This is used for ownership change of the install.'
                  type: string
                  format: int64
                  minimum: 1
                  example: '1234'
                user_email:
                  description: 'The email of the user. This is used for ownership change of the install.'
                  type: string
                  example: foo@example.com
                install_ids:
                  description: 'A comma seperated string of Install IDs. This is used for ownership change of the install.'
                  type: array
                  items: { type: string }
                  example: '1234,2478,2345'
              type: object
      responses:
        '200':
          description: 'Install updated'
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Install'
        '400':
          $ref: '#/components/responses/400'
        '401':
          $ref: '#/components/responses/401'
        '402':
          $ref: '#/components/responses/402'
        '404':
          $ref: '#/components/responses/404'
    delete:
      tags:
        - Installations
      summary: 'Delete an install'
      description: 'Delete a product install. This is different from an uninstall.'
      operationId: installations/delete-install
      responses:
        '204':
          $ref: '#/components/responses/204'
        '400':
          $ref: '#/components/responses/400'
        '401':
          $ref: '#/components/responses/401'
        '402':
          $ref: '#/components/responses/402'
        '404':
          $ref: '#/components/responses/404'
    parameters:
      -
        $ref: '#/components/parameters/product_id'
      -
        $ref: '#/components/parameters/install_id'
  '/products/{product_id}/installs.json':
    get:
      tags:
        - Installations
      summary: 'List all installs'
      description: "Retrieve the install collection associated with the product.\n\nVarious filtering and search parameters are available to narrow down the results."
      operationId: installations/list-installs
      parameters:
        -
          name: ids
          in: query
          description: 'Install IDs collection to filter.'
          schema:
            type: string
            format: comma-separated
            example: '1234,2478,2345'
        -
          name: filter
          in: query
          description: 'Install status to filter the installs by.'
          schema:
            type: string
            enum:
              - all
              - active
              - inactive
              - trial
              - paying
              - uninstalled
              - active_premium
              - active_free
        -
          name: version
          in: query
          description: 'Plugin version to filter the installs by.'
          schema:
            type: string
        -
          name: license_id
          in: query
          description: 'License ID to filter the installs by.'
          schema:
            type: integer
        -
          name: plan_id
          in: query
          description: 'Plan ID to filter the installs by.'
          schema:
            type: integer
        -
          name: title
          in: query
          description: 'Install title to filter the installs by.'
          schema:
            type: string
        -
          name: url
          in: query
          description: 'Install URL to filter the installs by.'
          schema:
            type: string
        -
          name: search
          in: query
          description: 'Search item to filter the installs by e.g. domain, site_id, or reason info.'
          schema:
            type: string
        -
          name: all
          in: query
          description: 'If true, loads all installs, including the uninstalled ones.'
          schema:
            type: boolean
            default: false
        -
          name: reason_id
          in: query
          description: 'Reason ID (either string or numeric) to filter the installs by.'
          schema:
            type: string
        -
          $ref: '#/components/parameters/count'
        -
          $ref: '#/components/parameters/offset'
        -
          $ref: '#/components/parameters/fields'
      responses:
        '200':
          description: 'Installs collection'
          content:
            application/json:
              schema:
                properties:
                  installs: { type: array, items: { $ref: '#/components/schemas/Install' } }
                type: object
        '400':
          $ref: '#/components/responses/400'
        '401':
          $ref: '#/components/responses/401'
        '402':
          $ref: '#/components/responses/402'
        '404':
          $ref: '#/components/responses/404'
    parameters:
      -
        $ref: '#/components/parameters/product_id'
  '/products/{product_id}/installs/{install_id}/license.json':
    get:
      tags:
        - Installations
      summary: 'Retrieve an active license by UID'
      description: "Retrieve the full information about the active license for the specified install when the UID of the install is known.\n\n> No Authorization header is required."
      operationId: installations/retrieve-active-license-by-uid
      parameters:
        -
          name: license_key
          in: query
          description: 'The license key used for the activation of the install.'
          required: true
          schema:
            $ref: '#/components/schemas/License/properties/secret_key'
        -
          $ref: '#/components/parameters/uid'
        -
          $ref: '#/components/parameters/fields'
      responses:
        '200':
          description: 'Successful operation'
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/License'
        '400':
          $ref: '#/components/responses/400'
        '402':
          $ref: '#/components/responses/402'
        '404':
          $ref: '#/components/responses/404'
      security: []
    parameters:
      -
        $ref: '#/components/parameters/install_id'
      -
        $ref: '#/components/parameters/product_id'
  '/products/{product_id}/installs/{install_id}/licenses/{license_id}.json':
    get:
      tags:
        - Installations
      summary: 'Retrieve an active license by ID'
      description: "Retrieve specific license of the install when the license ID and the license key are known but the UID of the install is not known.\n\n> Retrieve the license information with product level authorization when the UID of the install is unknown."
      operationId: installations/retrieve-active-license-by-id
      parameters:
        -
          $ref: '#/components/parameters/fields'
        -
          name: license_key
          in: query
          description: 'The license key used on the install.'
          required: true
          schema:
            $ref: '#/components/schemas/License/properties/secret_key'
      responses:
        '200':
          description: 'Install''s licence'
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/License'
        '400':
          $ref: '#/components/responses/400'
        '401':
          $ref: '#/components/responses/401'
        '402':
          $ref: '#/components/responses/402'
        '404':
          $ref: '#/components/responses/404'
    put:
      tags:
        - Installations
      summary: 'Activate a license'
      description: 'Activate license for an install.'
      operationId: installations/activate-license
      parameters:
        -
          name: license_key
          in: query
          description: 'The license key received from the checkout.'
          required: true
          schema:
            type: string
        -
          name: is_enriched
          in: query
          description: 'If `true`, the parent license''s and plan''s info will be included in the result if there''s any.'
          required: false
          schema:
            type: boolean
            default: false
      responses:
        '200':
          description: 'Activated licence.'
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/License'
        '400':
          $ref: '#/components/responses/400'
        '401':
          $ref: '#/components/responses/401'
        '402':
          $ref: '#/components/responses/402'
        '404':
          $ref: '#/components/responses/404'
    delete:
      tags:
        - Installations
      summary: 'Deactivate a license'
      description: 'Deactivate license from an install.'
      operationId: installations/deactivate-license
      parameters:
        -
          name: license_key
          in: query
          description: 'The same license key used to activate the install.'
          required: true
          schema:
            type: string
        -
          $ref: '#/components/parameters/fields'
      responses:
        '200':
          description: 'Activated licence.'
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/License'
        '400':
          $ref: '#/components/responses/400'
        '401':
          $ref: '#/components/responses/401'
        '402':
          $ref: '#/components/responses/402'
        '404':
          $ref: '#/components/responses/404'
    parameters:
      -
        $ref: '#/components/parameters/product_id'
      -
        $ref: '#/components/parameters/install_id'
      -
        $ref: '#/components/parameters/license_id'
  '/products/{product_id}/installs/{install_id}/licenses.json':
    get:
      tags:
        - Installations
      summary: 'List all active licenses'
      description: "Retrieve the active licenses (usually only one) on an install.\n\n> Use this endpoint only when the ID of the license is unknown."
      operationId: installations/list-active-licenses
      parameters:
        -
          name: is_enriched
          in: query
          description: 'If `true`, the parent license''s and plan''s info will be included in the result if there''s any.'
          required: false
          schema:
            type: boolean
            default: false
      responses:
        '200':
          description: 'Active license.'
          content:
            application/json:
              schema:
                properties:
                  licenses: { type: array, items: { $ref: '#/components/schemas/License' } }
                type: object
        '400':
          $ref: '#/components/responses/400'
        '401':
          $ref: '#/components/responses/401'
        '402':
          $ref: '#/components/responses/402'
        '404':
          $ref: '#/components/responses/404'
    parameters:
      -
        $ref: '#/components/parameters/product_id'
      -
        $ref: '#/components/parameters/install_id'
  '/products/{product_id}/installs/{install_id}/licenses/{license_id}/subscriptions.json':
    get:
      tags:
        - Licenses
      summary: 'List all subscriptions'
      description: "Retrieve the subscription collection associated with a license.\n\n> A license can have one active and multiple inactive subscriptions. Subscriptions are inactivated when a license is downgraded or upgraded or when the payment method is updated."
      operationId: licenses/list-subscriptions
      parameters:
        -
          $ref: '#/components/parameters/count'
        -
          $ref: '#/components/parameters/offset'
        -
          $ref: '#/components/parameters/fields'
      responses:
        '200':
          description: 'Subscriptions collection.'
          content:
            application/json:
              schema:
                properties:
                  subscriptions: { type: array, items: { $ref: '#/components/schemas/Subscription' } }
                type: object
        '400':
          $ref: '#/components/responses/400'
        '401':
          $ref: '#/components/responses/401'
        '402':
          $ref: '#/components/responses/402'
        '404':
          $ref: '#/components/responses/404'
    parameters:
      -
        $ref: '#/components/parameters/product_id'
      -
        $ref: '#/components/parameters/install_id'
      -
        $ref: '#/components/parameters/license_id'
  '/products/{product_id}/installs/{install_id}/market_items.json':
    get:
      tags:
        - Installations
      summary: 'List all market items'
      description: "Retrieves all market items associated with an `Install` entity.\n\n> Market items are other products (not necessarily powered by Freemius) that are installed in the same site as the Freemius powered product.\n\n> It is only after the user chooses to opt-in that such data is collected and sent to Freemius. Right now we only support WordPress products i.e. plugins and themes."
      operationId: installations/list-market-items
      responses:
        '200':
          description: 'All market items associated with the install.'
          content:
            application/json:
              schema:
                properties:
                  market_items: { type: array, items: { type: object, allOf: [{ $ref: '#/components/schemas/MarketItem' }] } }
                type: object
        '400':
          $ref: '#/components/responses/400'
        '401':
          $ref: '#/components/responses/401'
        '404':
          $ref: '#/components/responses/404'
    parameters:
      -
        $ref: '#/components/parameters/product_id'
      -
        $ref: '#/components/parameters/install_id'
  '/developer/{developer_id}/products/{product_id}/installs/{install_id}/members.json':
    post:
      tags:
        - Developers
      summary: 'Add team member'
      description: "Add new team member to the product.\n\n> Only a developer with priviledge can add a new team member to a product."
      operationId: developers/add-team-member
      requestBody:
        required: true
        content:
          application/json:
            schema:
              required:
                - role
              properties:
                role:
                  $ref: '#/components/schemas/Member/allOf/1/properties/role'
                member_id:
                  description: 'The id of the new member (Developer ID).'
                  type: string
                  format: int64
                  minimum: 1
                  example: '1234'
                email:
                  description: 'The email of the new member.'
                  type: string
                  example: foo@example.com
              type: object
      responses:
        '200':
          description: 'Team member added successfully.'
          content:
            application/json:
              schema:
                properties:
                  id: { description: 'The id of the team member.', type: number, example: 1234 }
                  email: { description: 'The email of the team member.', type: string, example: foo@example.com }
                  first: { description: 'The first name of the team member.', type: string, example: John }
                  last: { description: 'The last name of the team member.', type: string, example: Doe }
                  picture: { description: 'The picture of the team member.', type: string }
                  role: { $ref: '#/components/schemas/Member/allOf/1/properties/role' }
                  plugin_id: { $ref: '#/components/schemas/Member/allOf/1/properties/plugin_id' }
                type: object
        '400':
          $ref: '#/components/responses/400'
        '401':
          $ref: '#/components/responses/401'
        '402':
          $ref: '#/components/responses/402'
        '404':
          $ref: '#/components/responses/404'
      x-remove-from-doc: true
      x-internal: true
    parameters:
      -
        $ref: '#/components/parameters/product_id'
      -
        $ref: '#/components/parameters/install_id'
  '/products/{product_id}/installs/{install_id}/payments.json':
    get:
      tags:
        - Installations
      summary: 'List all payments'
      description: "Retrieve the payment associated with the install.\n\n> This lists all payments collected from the license activated on this install."
      operationId: installations/list-payments
      parameters:
        -
          name: extended
          in: query
          description: 'If `true`, loads linked user email, install URL, subscription billing cycle and plan name.'
          schema:
            type: boolean
            default: false
        -
          $ref: '#/components/parameters/count'
        -
          $ref: '#/components/parameters/offset'
        -
          $ref: '#/components/parameters/fields'
      responses:
        '200':
          description: 'Payments collection'
          content:
            application/json:
              schema:
                properties:
                  payments: { type: array, items: { allOf: [{ $ref: '#/components/schemas/Payment' }, { properties: { email: { $ref: '#/components/schemas/User/properties/email' }, url: { $ref: '#/components/schemas/Install/properties/url' }, billing_cycle: { $ref: '#/components/schemas/Subscription/properties/billing_cycle' }, plan_name: { $ref: '#/components/schemas/Plan/properties/name' }, refund_reason: { description: '512-character reason for the refund.', type: string, nullable: true } }, type: object }] } }
                type: object
        '400':
          $ref: '#/components/responses/400'
        '401':
          $ref: '#/components/responses/401'
        '402':
          $ref: '#/components/responses/402'
        '404':
          $ref: '#/components/responses/404'
    parameters:
      -
        $ref: '#/components/parameters/product_id'
      -
        $ref: '#/components/parameters/install_id'
  '/products/{product_id}/installs/{install_id}/permissions.json':
    put:
      tags:
        - Installations
      summary: 'Update permissions'
      description: 'Update permissions to a product install.'
      operationId: installations/update-permissions
      requestBody:
        required: true
        content:
          application/json:
            schema:
              properties:
                is_enabled:
                  description: 'Whether to enable the selected permission.'
                  type: boolean
                permissions:
                  description: 'Comma separated list of permissions to update. Allowed values are `site`, `user`, `extensions`.'
                  type: string
                  format: csv
                  example: 'site,user,extensions'
                  nullable: false
              type: object
      responses:
        '200':
          description: 'Install permission updated.'
          content:
            application/json:
              schema:
                allOf:
                  - { $ref: '#/components/schemas/InstallMetadata' }
        '400':
          $ref: '#/components/responses/400'
        '401':
          $ref: '#/components/responses/401'
        '402':
          $ref: '#/components/responses/402'
        '404':
          $ref: '#/components/responses/404'
    parameters:
      -
        $ref: '#/components/parameters/product_id'
      -
        $ref: '#/components/parameters/install_id'
  '/products/{product_id}/installs/{install_id}/plans/{plan_id}.json':
    get:
      tags:
        - Installations
      summary: 'Retrieve a plan'
      description: 'Retrieve the product plan details to which the install is subscribed.'
      operationId: installations/retrieve-plan
      parameters:
        -
          $ref: '#/components/parameters/fields'
      responses:
        '200':
          description: 'Install Plan'
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Plan'
        '400':
          $ref: '#/components/responses/400'
        '401':
          $ref: '#/components/responses/401'
        '402':
          $ref: '#/components/responses/402'
        '404':
          $ref: '#/components/responses/404'
    parameters:
      -
        $ref: '#/components/parameters/product_id'
      -
        $ref: '#/components/parameters/install_id'
      -
        $ref: '#/components/parameters/plan_id'
  '/products/{product_id}/installs/{install_id}/plans.json':
    get:
      tags:
        - Installations
      summary: 'List all plans'
      description: 'Retrieve all the available product plans to which an install can subscribe.'
      operationId: installations/list-plans
      parameters:
        -
          name: show_pending
          in: query
          description: 'Show all plans whether released to customers or hidden.'
          required: false
          schema:
            type: boolean
            default: false
        -
          $ref: '#/components/parameters/fields'
      responses:
        '200':
          description: 'Install Plans'
          content:
            application/json:
              schema:
                properties:
                  plans: { type: array, items: { $ref: '#/components/schemas/Plan' } }
                type: object
        '400':
          $ref: '#/components/responses/400'
        '401':
          $ref: '#/components/responses/401'
        '402':
          $ref: '#/components/responses/402'
        '404':
          $ref: '#/components/responses/404'
    parameters:
      -
        $ref: '#/components/parameters/product_id'
      -
        $ref: '#/components/parameters/install_id'
  '/products/{product_id}/installs/{install_id}/plans/{plan_id}/pricing/{pricing_id}/licenses.json':
    post:
      tags:
        - Installations
      summary: 'Create a new license'
      description: "Create a new license and assign it to the install.\n\n> Either `period` or `expires_at` must be set."
      operationId: installations/create-new-license
      parameters:
        -
          $ref: '#/components/parameters/fields'
      requestBody:
        required: true
        content:
          application/json:
            schema:
              properties:
                is_block_features:
                  $ref: '#/components/schemas/License/properties/is_block_features'
                period:
                  $ref: '#/components/schemas/Subscription/properties/billing_cycle'
                expires_at:
                  $ref: '#/components/schemas/License/properties/expiration'
                send_email:
                  description: 'Whether or not to email the license key and download link to the user.'
                  type: boolean
              type: object
      responses:
        '200':
          description: 'License created successfully.'
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/License'
        '400':
          $ref: '#/components/responses/400'
        '401':
          $ref: '#/components/responses/401'
        '402':
          $ref: '#/components/responses/402'
        '404':
          $ref: '#/components/responses/404'
    parameters:
      -
        $ref: '#/components/parameters/product_id'
      -
        $ref: '#/components/parameters/install_id'
      -
        $ref: '#/components/parameters/plan_id'
      -
        $ref: '#/components/parameters/pricing_id'
  '/products/{product_id}/installs/{install_id}/plans/{plan_id}/trials.json':
    post:
      tags:
        - Installations
      summary: 'Start a trial'
      description: 'Start the trial of a plan for which an install is subscribed. The install must not have utilized the trial before.'
      operationId: installations/start-trial
      parameters:
        -
          $ref: '#/components/parameters/fields'
      requestBody:
        required: true
        content:
          application/json:
            schema:
              properties:
                trial_ends:
                  description: 'The expiry date of the trial. If set, will set the trial expiration based on that parameter. **Note:** Trial expiration date cannot exceed the maximum trial period days based on the plan configuration.'
                  type: string
                  format: date-time
                  example: '2025-01-01 00:00:00'
                phone:
                  $ref: '#/components/schemas/Billing/properties/phone'
                is_migration:
                  description: 'Whether emails will be sent to users or log events. If `true`, no emails will be sent nor events logged.'
                  type: boolean
                trial_token:
                  description: 'Security token for sandbox mode trial.'
                  type: string
                trial_timestamp:
                  description: 'Security timestamp for sandbox mode trial.'
                  type: string
                  example: '1730160000'
              type: object
      responses:
        '200':
          description: 'Started Trial'
          content:
            application/json:
              schema:
                properties:
                  trial: { $ref: '#/components/schemas/Trial' }
                type: object
        '400':
          $ref: '#/components/responses/400'
        '401':
          $ref: '#/components/responses/401'
        '402':
          $ref: '#/components/responses/402'
        '404':
          $ref: '#/components/responses/404'
    parameters:
      -
        $ref: '#/components/parameters/product_id'
      -
        $ref: '#/components/parameters/install_id'
      -
        $ref: '#/components/parameters/plan_id'
  '/products/{product_id}/installs/{install_id}/trials.json':
    delete:
      tags:
        - Installations
      summary: 'Cancel a trial'
      description: 'Cancel a trial associated with a specific install.'
      operationId: installations/cancel-trial
      parameters:
        -
          name: reason_ids
          in: query
          description: 'Optional cancellation reason IDs.'
          schema:
            type: array
            items:
              $ref: '#/components/schemas/Uninstall/properties/reason_id'
        -
          parameter: reason
          name: reason
          in: query
          schema:
            $ref: '#/components/schemas/Uninstall/properties/reason_info'
        -
          $ref: '#/components/parameters/fields'
      responses:
        '200':
          description: 'The install with cancelled trial.'
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Install'
        '400':
          $ref: '#/components/responses/400'
        '401':
          $ref: '#/components/responses/401'
        '402':
          $ref: '#/components/responses/402'
        '404':
          $ref: '#/components/responses/404'
    parameters:
      -
        $ref: '#/components/parameters/product_id'
      -
        $ref: '#/components/parameters/install_id'
  '/products/{product_id}/installs/{install_id}/uninstall.json':
    get:
      tags:
        - Installations
      summary: 'Retrieve uninstall details'
      description: 'Retrieve the details of an install where the product has been uninstalled.'
      operationId: installations/retrieve-uninstall-details
      parameters:
        -
          $ref: '#/components/parameters/fields'
      responses:
        '200':
          description: 'The uninstall details.'
          content:
            application/json:
              schema:
                allOf:
                  - { $ref: '#/components/schemas/Uninstall' }
                  - { properties: { reason: { description: 'The reason for the uninstall which translates to the string value of the uninstall `reason_id`.', type: string } }, type: object }
        '400':
          $ref: '#/components/responses/400'
        '401':
          $ref: '#/components/responses/401'
        '404':
          $ref: '#/components/responses/404'
    parameters:
      -
        $ref: '#/components/parameters/product_id'
      -
        $ref: '#/components/parameters/install_id'
  '/products/{product_id}/installs/{install_id}/updates.json':
    get:
      tags:
        - Installations
      summary: 'List all updates'
      description: 'Retrieve the product update collection available for an install.'
      operationId: installations/list-updates
      parameters:
        -
          name: version
          in: query
          description: 'The product''s version of the current install. The endpoint will return newer versions when set. This is a required param unless `older_than` is provided.'
          required: true
          schema:
            type: string
            example: 1.0.0
        -
          name: older_than
          in: query
          description: 'If provided, only versions that are older than this will be returned.'
          schema:
            type: string
            example: 1.0.0
        -
          name: type
          in: query
          description: 'The product type. If the type provide is `all`, the latest `released` or `pending` version will be returned, whichever has the higher version.'
          schema:
            type: string
            default: released
            enum:
              - released
              - pending
              - beta
              - all
        -
          $ref: '#/components/parameters/count'
        -
          $ref: '#/components/parameters/offset'
        -
          $ref: '#/components/parameters/fields'
      responses:
        '200':
          description: 'Updates collection.'
          content:
            application/json:
              schema:
                properties:
                  tags: { type: array, items: { allOf: [{ $ref: '#/components/schemas/PluginTag' }, { properties: { is_released: { $ref: '#/components/schemas/Plugin/properties/is_released' }, url: { description: 'The Installation zip file URL with authentication token.', type: string, example: 'https://example.com/' } }, type: object }] } }
                type: object
        '400':
          $ref: '#/components/responses/400'
        '401':
          $ref: '#/components/responses/401'
        '404':
          $ref: '#/components/responses/404'
    parameters:
      -
        $ref: '#/components/parameters/product_id'
      -
        $ref: '#/components/parameters/install_id'
  '/products/{product_id}/installs/{install_id}/updates/latest.json':
    get:
      tags:
        - Installations
      summary: 'Retrieve the latest update'
      description: 'Retrieve the latest product update available for an install.'
      operationId: installations/retrieve-latest-update
      parameters:
        -
          name: is_premium
          in: query
          description: 'If set, tries to fetch the requested version. If requires premium but no license, will throw an error. Otherwise, fetch version based on license.'
          schema:
            type: boolean
        -
          name: readme
          in: query
          description: 'If set, tries to fetch the readme information.'
          schema:
            type: boolean
        -
          name: newer_than
          in: query
          description: 'If set, return the latest version''s data only if it''s newer than this property''s value.'
          schema:
            type: boolean
        -
          name: type
          in: query
          description: 'The product type. If the type provided is `all`, the latest `released`, `beta`,  or `pending` version will be returned, whichever has the higher version.'
          schema:
            type: string
            default: released
            enum:
              - released
              - pending
              - beta
              - all
      responses:
        '200':
          description: 'Updates collection.'
          content:
            application/json:
              schema:
                allOf:
                  - { $ref: '#/components/schemas/PluginTag' }
                  - { properties: { is_released: { $ref: '#/components/schemas/Plugin/properties/is_released' }, url: { description: 'The Installation zip file URL with authorization token.', type: string, example: 'https://example.com/' } }, type: object }
        '400':
          $ref: '#/components/responses/400'
        '401':
          $ref: '#/components/responses/401'
        '402':
          $ref: '#/components/responses/402'
        '404':
          $ref: '#/components/responses/404'
    parameters:
      -
        $ref: '#/components/parameters/product_id'
      -
        $ref: '#/components/parameters/install_id'
  '/products/{product_id}/installs/{install_id}/users/{user_id}/ownership-change.json':
    put:
      tags:
        - Installations
      summary: 'Change ownership'
      description: 'Change ownership of an install.'
      operationId: installations/change-ownership
      requestBody:
        required: true
        content:
          application/json:
            schema:
              required:
                - token_salt
                - email
              properties:
                token_salt:
                  description: 'The transfer token salt. This is generated by Freemius and sent over email with expiration.'
                email:
                  description: 'Candidate or owner email.'
                transfer_type:
                  description: 'Defaults to ''transfer'' for backward compatibility.'
                owner_token:
                  description: 'Token generated by Freemius. Get this from the [Developer Dashboard](https://dashboard.freemius.com).'
                candidate_token:
                  description: 'Token generated by Freemius. Get this from the [Developer Dashboard](https://dashboard.freemius.com).'
                after_confirm_url:
                  description: 'The URL to redirect after the user confirms the ownership change.'
                install_ids:
                  description: 'Comma-separated list of IDs of installs that should be transferred to the new owner. This can include add-ons'' install IDs.'
              type: object
      responses:
        '200':
          description: 'Install ownership changed successfully. No response will be sent, but it will be redirected to the `after_confirm_url` if it was used when initiating the ownership transfer.'
        '400':
          $ref: '#/components/responses/400'
        '401':
          $ref: '#/components/responses/401'
        '402':
          $ref: '#/components/responses/402'
        '404':
          $ref: '#/components/responses/404'
      x-remove-from-doc: true
      x-internal: true
    parameters:
      -
        $ref: '#/components/parameters/product_id'
      -
        $ref: '#/components/parameters/install_id'
      -
        $ref: '#/components/parameters/user_id'
  '/products/{product_id}/installs/{install_id}/users/{user_id}/verify.json':
    put:
      tags:
        - Installations
      summary: 'Send a verification email'
      description: "Sends an email to the user associated with the install, containing a link to verify the email address.\n\n> With the `after_email_confirm_url` parameter, you can specify a URL address that the user will be auto forwarded to after email confirmation is clicked."
      operationId: installations/send-verification-email
      requestBody:
        required: true
        content:
          application/json:
            schema:
              properties:
                after_email_confirm_url:
                  description: 'URL address that the user will be auto forwarded to after email confirmation is clicked.'
                  type: string
                  example: 'https://example.com/email-confirmation/'
              type: object
      responses:
        '200':
          description: 'Successful operation.'
        '400':
          $ref: '#/components/responses/400'
        '401':
          $ref: '#/components/responses/401'
        '402':
          $ref: '#/components/responses/402'
        '404':
          $ref: '#/components/responses/404'
      x-remove-from-doc: true
      x-internal: true
    parameters:
      -
        $ref: '#/components/parameters/product_id'
      -
        $ref: '#/components/parameters/install_id'
      -
        $ref: '#/components/parameters/user_id'
  '/products/{product_id}/is_active.json':
    get:
      tags:
        - Products
      summary: 'Check product status'
      description: 'Check if the product is active.'
      operationId: products/check-status
      parameters:
        -
          name: is_update
          in: query
          description: "You can use this flag in conjunction with the Moderation Setting of your product.\n\nIn case you want to limit the activation of your product to new instances only (say after migrating to Freemius) you can check the relevant settings from the Developer Dashboard and from your product make an API request like below:\n\n- If your product is already active in some device before joining Freemius - Set value to `true`.\n- Otherwise set value to `false`.\n\nThis will also work with any “Activation limitation” you have put in your Moderation settings."
          required: false
          schema:
            type: boolean
            default: false
      responses:
        '200':
          description: 'Product status.'
          content:
            application/json:
              schema:
                properties:
                  is_active: { description: 'The product status.', type: boolean }
                  timestamp: { description: 'The timestamp when the product status was done.', type: integer, format: int64, example: 1742454772 }
                type: object
        '400':
          $ref: '#/components/responses/400'
        '401':
          $ref: '#/components/responses/401'
        '402':
          $ref: '#/components/responses/402'
        '404':
          $ref: '#/components/responses/404'
    parameters:
      -
        $ref: '#/components/parameters/product_id'
  '/products/{product_id}/licenses/activate.json':
    post:
      tags:
        - Licenses
      summary: 'Activate a license'
      description: "Activate a license and if needed, create an install with the given properties.\n\n> No Authorization header is required. If the provided license doesn't have an associated user, the endpoint will require the `first_name`, `last_name`, and `user_email` parameters to create a new user and associate it with the license.\n\nThis endpoint can return the following error codes:\n\n- `license_expired`: License has already expired.\n- `invalid_license_key`: License key is invalid (e.g., does not match any record).\n- `license_error`: General error while validating the license.\n- `license_utilized`: License quota has reached maximum capacity.\n- `license_activated`: License is already activated on the given install. This usually indicates your app is out of sync with Freemius. You may accept the license and grant premium features. If needed, re-establish the connection by calling the [deactivation endpoint](../licenses/deactivate) and activating again.\n\nAll errors include a descriptive message from the API, which you may choose to display to the user. For example:\n\n- `license_expired`: Your license has expired on 2025-01-01 (id = 12345).\n- `invalid_license_key`: Invalid license key.\n- `license_error`: License activation is not authorized for the site(s) listed below. Please follow the provided link to whitelist the site(s) from the User Dashboard.\n- `license_activated`: License is already activated on install 12345.\n- `license_utilized`: Your license quota of 1234 production site(s) has been reached. If you believe this is a mistake, please contact support at example@freemius.com.\n\nYou can get the error code from the `response.error.code`. For example\n\n```js\nfetch(activationEndpoint).then((response) => {\n    return response.json();\n}).then((data) => {\n    if (data.error) {\n        // Error detected\n        const errorCode = data.error.code;\n        const errorMessage = data.error.message;\n        // handleError(errorCode, errorMessage);\n    } else {\n        // Operation successful\n    }\n}).catch((error) => {\n    // Handle network error\n});\n``` "
      operationId: licenses/activate
      requestBody:
        required: true
        content:
          application/json:
            schema:
              required:
                - uid
                - license_key
              properties:
                uid:
                  $ref: '#/components/schemas/CommonProperties/properties/uid'
                license_key:
                  $ref: '#/components/schemas/License/properties/secret_key'
                url:
                  description: 'Site''s homepage URL.'
                  type: string
                title:
                  description: 'Site''s title.'
                  type: string
                version:
                  description: 'Product''s version.'
                  type: string
                is_marketing_allowed:
                  $ref: '#/components/schemas/User/properties/is_marketing_allowed'
                install_id:
                  description: 'Install ID when activating on an already existing install. If provided must belong to the same user as the license owner and must have the same UID. The new license will be activated for the install and existing one will be deactivated.'
                  type: integer
                first_name:
                  description: 'First name of the user (only needed when activating a ghost license).'
                  type: string
                last_name:
                  description: 'Last name of the user (only needed when activating a ghost license).'
                  type: string
                user_email:
                  description: 'Email address of the user (only needed when activating a ghost license).'
                  type: string
                allow_unreleased_plan_activation:
                  description: 'Whether to allow license activation if the plans of the product has not been released yet. Useful for testing purpose only.'
                  type: boolean
              type: object
      responses:
        '200':
          description: 'License activated successfully.'
          content:
            application/json:
              schema:
                properties:
                  user_id: { $ref: '#/components/schemas/User/properties/id' }
                  user_secret_key: { $ref: '#/components/schemas/User/properties/secret_key' }
                  user_public_key: { $ref: '#/components/schemas/User/properties/public_key' }
                  plugin_id: { $ref: '#/components/schemas/Plugin/properties/id' }
                  license_plan_name: { $ref: '#/components/schemas/Plan/properties/name' }
                  is_marketing_allowed: { $ref: '#/components/schemas/User/properties/is_marketing_allowed' }
                  install_id: { $ref: '#/components/schemas/Install/properties/id' }
                  install_secret_key: { $ref: '#/components/schemas/Install/properties/secret_key' }
                  install_public_key: { $ref: '#/components/schemas/Install/properties/public_key' }
                  install_api_token: { description: 'The API access token with which authenticated requests can be made for this `install` entity. You need to set this token as the `Bearer` token in the `Authorization` header. For example: <pre>Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9</pre>', type: string, example: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9 }
                type: object
        '400':
          $ref: '#/components/responses/400'
        '402':
          $ref: '#/components/responses/402'
        '404':
          $ref: '#/components/responses/404'
      security: []
    parameters:
      -
        $ref: '#/components/parameters/product_id'
  '/products/{product_id}/licenses/{license_id}/checkout/link.json':
    post:
      tags:
        - Licenses
      summary: 'Generate upgrade link'
      description: 'Generate an upgrade link for a license. The API accepts a variety of parameters with which you can specify new plans or quota or billing cycles. If you skip all those, then a manual renewal link will be generated instead. The link will be valid for 24 hours.'
      operationId: licenses/generate-upgrade-link
      requestBody:
        required: true
        content:
          application/json:
            schema:
              properties:
                plan_id:
                  description: 'The plan ID to upgrade to.'
                  type: string
                  format: int64
                  minimum: 0
                billing_cycle:
                  $ref: '#/components/schemas/CommonEnums/properties/PlanPeriod'
                quota:
                  description: 'The quota to use. Can be a number or the string ''unlimited''.'
                  oneOf: [{ type: integer, minimum: 1 }, { type: string, enum: [unlimited] }]
                is_payment_method_update:
                  description: 'Whether to update the payment method. If true, the link will be generated for the current plan and billing cycle of the license and other parameters will be ignored. If the license is not associated with a subscription, or is lifetime, an exception will be thrown.'
                  type: boolean
                  default: false
              type: object
      responses:
        '201':
          description: 'Upgrade link generated successfully.'
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/CheckoutUpgradeLink'
        '400':
          $ref: '#/components/responses/400'
        '402':
          $ref: '#/components/responses/402'
        '404':
          $ref: '#/components/responses/404'
    parameters:
      -
        $ref: '#/components/parameters/product_id'
      -
        $ref: '#/components/parameters/license_id'
  '/products/{product_id}/licenses/deactivate.json':
    post:
      tags:
        - Licenses
      summary: 'Deactivate a license'
      description: 'Deactivate a license from an install (No Authorization header is required).'
      operationId: licenses/deactivate
      parameters:
        -
          $ref: '#/components/parameters/fields'
      requestBody:
        required: true
        content:
          application/json:
            schema:
              required:
                - uid
                - install_id
                - license_key
              properties:
                uid:
                  $ref: '#/components/schemas/CommonProperties/properties/uid'
                install_id:
                  description: 'Install ID from which the license should be deactivated. The license must be active on the install.'
                  type: integer
                license_key:
                  $ref: '#/components/schemas/License/properties/secret_key'
              type: object
      responses:
        '200':
          description: 'License deactivated.'
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Install'
        '400':
          $ref: '#/components/responses/400'
        '401':
          $ref: '#/components/responses/401'
        '402':
          $ref: '#/components/responses/402'
        '404':
          $ref: '#/components/responses/404'
      security: []
    parameters:
      -
        $ref: '#/components/parameters/product_id'
  '/products/{product_id}/licenses/{license_id}.json':
    get:
      tags:
        - Licenses
      summary: 'Retrieve a license'
      description: 'Retrieve a specific license by its ID.'
      operationId: licenses/retrieve
      parameters:
        -
          $ref: '#/components/parameters/fields'
      responses:
        '200':
          description: 'The retrieved license.'
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/License'
        '400':
          $ref: '#/components/responses/400'
        '401':
          $ref: '#/components/responses/401'
        '402':
          $ref: '#/components/responses/402'
        '404':
          $ref: '#/components/responses/404'
    put:
      tags:
        - Licenses
      summary: 'Update a license'
      description: 'Update a specific license by its ID. For ownership transfer please use the `new_user_id`. Ownership transfer is not supported for SaaS products.'
      operationId: licenses/update
      parameters:
        -
          $ref: '#/components/parameters/fields'
      requestBody:
        required: false
        content:
          application/json:
            schema:
              properties:
                quota:
                  $ref: '#/components/schemas/License/properties/quota'
                expiration:
                  $ref: '#/components/schemas/License/properties/expiration'
                is_block_features:
                  $ref: '#/components/schemas/License/properties/is_block_features'
                is_whitelabeled:
                  $ref: '#/components/schemas/License/properties/is_whitelabeled'
                is_free_localhost:
                  $ref: '#/components/schemas/License/properties/is_free_localhost'
                new_user_id:
                  $ref: '#/components/schemas/License/properties/user_id'
                cancel_subscription:
                  description: '(optional) When set to `true` will cancel the subscription.'
                  type: boolean
                  example: true
                extend_bundle:
                  description: '(optional) When set to `true` to extend the bundle license.'
                  type: boolean
                  example: true
                update_subscription_renewal_date:
                  description: '(optional) When set to `true`, it will update the relevant (subscription renewal or trial end) date to 24 hours before license expiration.'
                  type: boolean
                  example: true
              type: object
      responses:
        '200':
          description: 'The updated license.'
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/License'
        '400':
          $ref: '#/components/responses/400'
        '401':
          $ref: '#/components/responses/401'
        '402':
          $ref: '#/components/responses/402'
        '404':
          $ref: '#/components/responses/404'
    delete:
      tags:
        - Licenses
      summary: 'Cancel a license'
      description: 'Cancel or delete a license. The Delete action is irreversible and will remove the license from the system.'
      operationId: licenses/cancel
      parameters:
        -
          name: delete
          in: query
          description: '(optional) Whether to delete the license. If not `true` then the license is cancelled.'
          required: false
          schema:
            type: boolean
            example: true
        -
          name: include_bundle
          in: query
          description: '(optional) Whether to include the bundle license in the deletion or delete the main license only.'
          required: false
          schema:
            type: boolean
            example: true
        -
          $ref: '#/components/parameters/fields'
      responses:
        '200':
          $ref: '#/components/schemas/License'
        '204':
          $ref: '#/components/responses/204'
        '400':
          $ref: '#/components/responses/400'
        '401':
          $ref: '#/components/responses/401'
        '402':
          $ref: '#/components/responses/402'
        '404':
          $ref: '#/components/responses/404'
    parameters:
      -
        $ref: '#/components/parameters/product_id'
      -
        $ref: '#/components/parameters/license_id'
  '/products/{product_id}/licenses.json':
    get:
      tags:
        - Licenses
      summary: 'List all licenses'
      description: 'Retrieve the license collection associated with a product.'
      operationId: licenses/list
      parameters:
        -
          name: filter
          in: query
          description: 'Filter licenses by status.'
          schema:
            type: string
            enum:
              - active
              - cancelled
              - expired
              - abandoned
              - migrated
            example: active
        -
          name: plan_id
          in: query
          description: 'Filter licenses by plan ID.'
          schema:
            type: number
            example: 123
        -
          name: search
          in: query
          description: 'Search license id or key.'
          schema:
            type: string
            example: '123'
        -
          name: enriched
          in: query
          description: 'If `true`, returns the associated user information.'
          schema:
            type: boolean
            default: false
            example: true
        -
          $ref: '#/components/parameters/count'
        -
          $ref: '#/components/parameters/offset'
        -
          $ref: '#/components/parameters/fields'
        -
          name: source
          in: query
          description: 'If set, returns only licenses that are associated with the given source ID.'
          schema:
            type: number
            example: 123
      responses:
        '200':
          description: 'The licenses collection is retrieved.'
          content:
            application/json:
              schema:
                properties:
                  licenses: { type: array, items: { $ref: '#/components/schemas/LicenseEnriched' } }
                type: object
        '400':
          $ref: '#/components/responses/400'
        '401':
          $ref: '#/components/responses/401'
        '402':
          $ref: '#/components/responses/402'
        '404':
          $ref: '#/components/responses/404'
    put:
      tags:
        - Licenses
      summary: 'Assign a license'
      description: 'Associate an orphan license with a user and send a welcome email. If the user does not exist yet, one will be created.'
      operationId: licenses/assign
      parameters:
        -
          $ref: '#/components/parameters/fields'
      requestBody:
        required: true
        content:
          application/json:
            schema:
              required:
                - email
                - license_key
              properties:
                email:
                  description: 'User''s email address.'
                  type: string
                  example: foo@example.com
                name:
                  description: 'User''s full name.'
                  type: string
                  example: 'John Doe'
                license_key:
                  $ref: '#/components/schemas/License/properties/secret_key'
                is_marketing_allowed:
                  $ref: '#/components/schemas/User/properties/is_marketing_allowed'
              type: object
      responses:
        '200':
          description: 'The license is assigned.'
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/License'
        '400':
          $ref: '#/components/responses/400'
        '401':
          $ref: '#/components/responses/401'
        '402':
          $ref: '#/components/responses/402'
        '404':
          $ref: '#/components/responses/404'
    parameters:
      -
        $ref: '#/components/parameters/product_id'
  '/products/{product_id}/licenses/{license_id}/installs.json':
    delete:
      tags:
        - Licenses
      summary: 'Deactivate installs'
      description: 'Deactivate license from all installs.'
      operationId: licenses/deactivate-installs
      parameters:
        -
          $ref: '#/components/parameters/fields'
      responses:
        '200':
          description: 'Licenses deactivated from all installs.'
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/License'
        '400':
          $ref: '#/components/responses/400'
        '401':
          $ref: '#/components/responses/401'
        '402':
          $ref: '#/components/responses/402'
        '404':
          $ref: '#/components/responses/404'
    parameters:
      -
        $ref: '#/components/parameters/product_id'
      -
        $ref: '#/components/parameters/license_id'
  '/developers/{developer_id}/products/{product_id}/licenses/{license_id}/installs/sync.json':
    post:
      tags:
        - Licenses
      summary: 'Sync all activations'
      description: 'Sync all the license activations with the actual available installs.'
      operationId: licenses/sync-activations
      parameters:
        -
          $ref: '#/components/parameters/fields'
      responses:
        '200':
          description: 'License activations synced.'
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/License'
        '400':
          $ref: '#/components/responses/400'
        '401':
          $ref: '#/components/responses/401'
        '402':
          $ref: '#/components/responses/402'
        '404':
          $ref: '#/components/responses/404'
      security:
        -
          ApiAuthFSACookie: []
        -
          ApiAuthFSAHeader: []
      x-remove-from-doc: true
      x-internal: true
    parameters:
      -
        $ref: '#/components/parameters/product_id'
      -
        $ref: '#/components/parameters/developer_id'
      -
        $ref: '#/components/parameters/license_id'
  '/products/{product_id}/licenses/{license_id}/renewals.json':
    post:
      tags:
        - Licenses
      summary: 'Send the renewal email'
      description: 'Send the manual license renewal email. The system will send emails only for licenses with cancelled or inactive subscriptions.'
      operationId: licenses/send-renewal-email
      responses:
        '200':
          description: 'The license renewal email is sent.'
          content:
            application/json:
              schema:
                properties:
                  sent: { description: 'Whether the email is sent.', type: boolean }
                type: object
        '400':
          $ref: '#/components/responses/400'
        '401':
          $ref: '#/components/responses/401'
        '402':
          $ref: '#/components/responses/402'
        '404':
          $ref: '#/components/responses/404'
    parameters:
      -
        $ref: '#/components/parameters/product_id'
      -
        $ref: '#/components/parameters/license_id'
  '/products/{product_id}/licenses/resend.json':
    post:
      tags:
        - Licenses
      summary: 'Resend license keys'
      description: 'Send an email from Freemius with all the license keys associated with the given email address. The email is sent to the email address.'
      operationId: licenses/resend-keys
      requestBody:
        required: true
        content:
          application/json:
            schema:
              required:
                - email
              properties:
                email:
                  description: 'The user''s email address associated with the license.'
                  type: string
                  example: johndoe@example.com
              type: object
      responses:
        '200':
          description: 'The license key has been resent.'
        '400':
          $ref: '#/components/responses/400'
        '401':
          $ref: '#/components/responses/401'
        '402':
          $ref: '#/components/responses/402'
        '404':
          $ref: '#/components/responses/404'
    parameters:
      -
        $ref: '#/components/parameters/product_id'
  '/products/{product_id}/licenses/{license_id}/resend.json':
    post:
      tags:
        - Licenses
      summary: 'Resend the upgrade email'
      description: 'Resend the license upgrade email.'
      operationId: licenses/resend-upgrade-email
      responses:
        '200':
          description: 'License email resent.'
        '400':
          $ref: '#/components/responses/400'
        '401':
          $ref: '#/components/responses/401'
        '402':
          $ref: '#/components/responses/402'
        '404':
          $ref: '#/components/responses/404'
    parameters:
      -
        $ref: '#/components/parameters/product_id'
      -
        $ref: '#/components/parameters/license_id'
  '/products/{product_id}/licenses/{license_id}/subscription.json':
    get:
      tags:
        - Licenses
      summary: 'Retrieve latest subscription'
      description: "A license can have only **one active subscription** at any given time. However, users may **upgrade**, **downgrade**, or **change their payment method**, which may result in a new subscription being created and associated with the same license.\n\nUse this endpoint to **retrieve the latest or currently active subscription** linked to a specific license.\n\nThis is useful when you're building tools for license management or need to inspect the billing state of a customer. If you're integrating Freemius with your SaaS please refer to our [guide here](help-documentation-selling-with-freemius-saas-integration.md)."
      operationId: licenses/retrieve-latest-subscription
      parameters:
        -
          $ref: '#/components/parameters/fields'
      responses:
        '200':
          description: 'Subscription retrieved.'
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Subscription'
        '401':
          $ref: '#/components/responses/401'
        '402':
          $ref: '#/components/responses/402'
        '404':
          $ref: '#/components/responses/404'
    delete:
      tags:
        - Licenses
      summary: 'Cancel current subscription'
      description: "Use this endpoint to **cancel the active subscription** associated with a license. If the license is currently in a **trialing state**, this will also cancel the trial.\n\nThis is useful when you want to programmatically offer a cancellation feature from within your SaaS or custom dashboards. If you're integrating Freemius with your SaaS, please see our [guide here](help-documentation-selling-with-freemius-saas-integration.md).\n\n> ⚠️ This action is irreversible and will immediately cancel the subscription or trial.\n\nCancelling an already cancelled subscription will not have any effect and the endpoint will return the same subscription details as before."
      operationId: licenses/cancel-current-subscription
      parameters:
        -
          name: reason_ids
          in: query
          description: 'Optional cancellation reason IDs.'
          schema:
            type: array
            items:
              $ref: '#/components/schemas/Uninstall/properties/reason_id'
        -
          parameter: reason
          name: reason
          in: query
          schema:
            $ref: '#/components/schemas/Uninstall/properties/reason_info'
      responses:
        '200':
          description: 'Subscription retrieved.'
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Subscription'
        '401':
          $ref: '#/components/responses/401'
        '402':
          $ref: '#/components/responses/402'
        '404':
          $ref: '#/components/responses/404'
    parameters:
      -
        $ref: '#/components/parameters/product_id'
      -
        $ref: '#/components/parameters/license_id'
  '/products/{product_id}/payments/{payment_id}.json':
    get:
      tags:
        - Payments
      summary: 'Retrieve a payment'
      description: 'Retrieve a specific payment.'
      operationId: payments/retrieve
      parameters:
        -
          $ref: '#/components/parameters/fields'
      responses:
        '200':
          description: 'Retrieve a specific payment.'
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Payment'
        '400':
          $ref: '#/components/responses/400'
        '401':
          $ref: '#/components/responses/401'
        '402':
          $ref: '#/components/responses/402'
        '404':
          $ref: '#/components/responses/404'
    parameters:
      -
        $ref: '#/components/parameters/product_id'
      -
        $ref: '#/components/parameters/payment_id'
  '/products/{product_id}/payments.json':
    get:
      tags:
        - Payments
      summary: 'List all payments'
      description: "Retrieve the payment collection associated with the product.\n\n### Filtering and searching\n\nYou search and/or filter payments with these parameters:\n\n- `search` - You can search by `payment_id`, `external_payment_id`, or `user_email`. It can be a number or string.\n- `user_id` - If you are looking to list all payments for a specific user use this.\n- `billing_cycle` - Filter payments by billing cycle. `0` means lifetime payments.\n- `currency` - Filter payments by currency.\n- `coupon_id` - Filter payments by coupon ID.\n- `filter` - Filter payments by different types: `all`, `refunds`, `not_refunded`, `disputed`, `won_disputes`, `chargebacks`.\n\nPlease see the parameters in the responses body for more information."
      operationId: payments/list
      parameters:
        -
          name: search
          in: query
          description: 'Search by `payment_id`, `external_payment_id`, or `user_email`.'
          schema:
            type: string
        -
          name: search_user_id
          in: query
          description: 'User ID to filter with.'
          schema:
            $ref: '#/components/schemas/CommonProperties/properties/user_id'
        -
          $ref: '#/components/parameters/billing_cycle'
        -
          name: currency
          in: query
          schema:
            $ref: '#/components/schemas/CommonEnums/properties/Currency'
        -
          name: coupon_id
          in: query
          description: 'Filter payments by coupon ID.'
          schema:
            $ref: '#/components/schemas/CommonProperties/properties/id'
        -
          name: filter
          in: query
          description: 'Filter payments by different types'
          schema:
            type: string
            default: all
            enum:
              - all
              - refunds
              - not_refunded
              - disputed
              - won_disputes
              - chargebacks
        -
          name: extended
          in: query
          description: 'If true, loads linked user, plan and subscription.'
          schema:
            type: boolean
            default: false
        -
          $ref: '#/components/parameters/to'
        -
          $ref: '#/components/parameters/from'
        -
          $ref: '#/components/parameters/count'
        -
          $ref: '#/components/parameters/offset'
        -
          $ref: '#/components/parameters/fields'
      responses:
        '200':
          description: 'The payment collection.'
          content:
            application/json:
              schema:
                properties:
                  payments: { type: array, items: { allOf: [{ $ref: '#/components/schemas/Payment' }, { properties: { email: { $ref: '#/components/schemas/User/properties/email' }, url: { $ref: '#/components/schemas/Install/properties/url' }, billing_cycle: { $ref: '#/components/schemas/Subscription/properties/billing_cycle' }, plan_name: { description: 'Name of the plan the payment is associated with.', type: string }, refund_reason: { description: 'If the payment is refunded, this will contain the reason.', type: string } }, type: object }] } }
                  discounts: { type: array, items: { $ref: '#/components/schemas/Discount' } }
                type: object
        '400':
          $ref: '#/components/responses/400'
        '401':
          $ref: '#/components/responses/401'
        '402':
          $ref: '#/components/responses/402'
        '404':
          $ref: '#/components/responses/404'
    parameters:
      -
        $ref: '#/components/parameters/product_id'
  '/products/{product_id}/payments/{payment_id}/invoice.pdf':
    get:
      tags:
        - Payments
      summary: 'Download invoice'
      description: 'Download invoice of a payment.'
      operationId: payments/download-invoice
      parameters:
        -
          $ref: '#/components/parameters/fields'
      responses:
        '200':
          description: 'PDF invoice'
          content:
            application/pdf: {  }
        '400':
          $ref: '#/components/responses/400'
        '401':
          $ref: '#/components/responses/401'
        '402':
          $ref: '#/components/responses/402'
        '404':
          $ref: '#/components/responses/404'
    parameters:
      -
        $ref: '#/components/parameters/product_id'
      -
        $ref: '#/components/parameters/payment_id'
  '/products/{product_id}/ping.json':
    get:
      tags:
        - Products
      summary: 'GDPR compliance check'
      description: 'Find out if a product requires GDPR compliance based on the client''s location.'
      operationId: products/gdpr-compliance-check
      parameters:
        -
          name: uid
          in: query
          description: 'Unique identifier of the caller. The UID must be same when pinging and when activating or deactivating a license. The generation of the UID is a responsibility of the client.'
          required: true
          schema:
            $ref: '#/components/schemas/CommonProperties/properties/uid'
        -
          name: is_update
          in: query
          description: 'If the call is during a product update.'
          schema:
            type: boolean
            default: false
        -
          name: is_gdpr_test
          in: query
          description: 'Whether the request is made for testing GDPR compliance from the client of the product.'
          schema:
            type: boolean
            default: false
      responses:
        '200':
          description: 'Response from the product'
          content:
            application/json:
              schema:
                properties:
                  api: { description: 'Just a "pong" to annotate the success.', type: string, enum: [pong], example: pong }
                  is_gdpr_required: { description: 'Whether GDPR compliance is required for the client.', type: boolean, example: false }
                  timestamp: { description: 'Timestamp in [RFC 2822](http://www.faqs.org/rfcs/rfc2822) or [RFC 5322](http://www.faqs.org/rfcs/rfc5322) format.', type: string, format: rfc-2822, example: 'Thu, 21 Jan 2021 12:00:00 +0000' }
                  is_active: { description: 'Whether the product is active. Only returned when `is_update` is true in the request.', type: boolean, example: true }
                type: object
        '400':
          $ref: '#/components/responses/400'
        '401':
          $ref: '#/components/responses/401'
        '404':
          $ref: '#/components/responses/404'
      x-remove-from-doc: true
      x-internal: true
    parameters:
      -
        $ref: '#/components/parameters/product_id'
  '/products/{product_id}/plans/currencies.json':
    get:
      tags:
        - Plans
      summary: 'List all currencies'
      description: 'Retrieve all the currencies available for all the plans.'
      operationId: plans/list-currencies
      responses:
        '200':
          description: 'The list of all currencies for all the plans.'
          content:
            application/json:
              schema:
                properties:
                  currencies: { type: array, items: { $ref: '#/components/schemas/CommonEnums/properties/Currency' } }
                type: object
        '400':
          $ref: '#/components/responses/400'
        '401':
          $ref: '#/components/responses/401'
        '402':
          $ref: '#/components/responses/402'
        '404':
          $ref: '#/components/responses/404'
    parameters:
      -
        $ref: '#/components/parameters/product_id'
  '/products/{product_id}/plans/{plan_id}/features.json':
    get:
      tags:
        - Plans
      summary: 'List all features'
      description: 'Retrieve the features collection of a plan.'
      operationId: plans/list-features
      parameters:
        -
          $ref: '#/components/parameters/count'
        -
          $ref: '#/components/parameters/offset'
        -
          $ref: '#/components/parameters/fields'
      responses:
        '200':
          description: 'Feature listing of a plan.'
          content:
            application/json:
              schema:
                properties:
                  features: { type: array, items: { allOf: [{ $ref: '#/components/schemas/Feature' }, { $ref: '#/components/schemas/FeaturePlan' }] } }
                type: object
        '400':
          $ref: '#/components/responses/400'
        '401':
          $ref: '#/components/responses/401'
        '402':
          $ref: '#/components/responses/402'
        '404':
          $ref: '#/components/responses/404'
    parameters:
      -
        $ref: '#/components/parameters/product_id'
      -
        $ref: '#/components/parameters/plan_id'
  '/products/{product_id}/plans/{plan_id}.json':
    get:
      tags:
        - Plans
      summary: 'Retrieve a plan'
      description: 'Retrieve a specific plan by ID.'
      operationId: plans/retrieve
      parameters:
        -
          $ref: '#/components/parameters/fields'
      responses:
        '200':
          description: 'Plan listing.'
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Plan'
        '400':
          $ref: '#/components/responses/400'
        '401':
          $ref: '#/components/responses/401'
        '402':
          $ref: '#/components/responses/402'
        '404':
          $ref: '#/components/responses/404'
    parameters:
      -
        $ref: '#/components/parameters/product_id'
      -
        $ref: '#/components/parameters/plan_id'
  '/products/{product_id}/plans.json':
    get:
      tags:
        - Plans
      summary: 'List all plans'
      description: 'Retrieve the plans collection.'
      operationId: plans/list
      parameters:
        -
          $ref: '#/components/parameters/fields'
      responses:
        '200':
          description: 'List of all the plans.'
          content:
            application/json:
              schema:
                properties:
                  plans: { type: array, items: { $ref: '#/components/schemas/Plan' } }
                type: object
        '400':
          $ref: '#/components/responses/400'
        '401':
          $ref: '#/components/responses/401'
        '402':
          $ref: '#/components/responses/402'
        '404':
          $ref: '#/components/responses/404'
    parameters:
      -
        $ref: '#/components/parameters/product_id'
  '/developers/{developer_id}/products/{product_id}/plans.json':
    post:
      tags:
        - Plans
      summary: 'Create a plan'
      description: 'Create a new plan for the product.'
      operationId: plans/create
      parameters:
        -
          $ref: '#/components/parameters/developer_id'
        -
          $ref: '#/components/parameters/fields'
      requestBody:
        required: true
        content:
          application/json:
            schema:
              properties:
                name:
                  $ref: '#/components/schemas/Plan/properties/name'
                title:
                  $ref: '#/components/schemas/Plan/properties/title'
                description:
                  $ref: '#/components/schemas/Plan/properties/description'
                is_free_localhost:
                  $ref: '#/components/schemas/Plan/properties/is_free_localhost'
                is_block_features:
                  $ref: '#/components/schemas/Plan/properties/is_block_features'
                is_block_features_monthly:
                  $ref: '#/components/schemas/Plan/properties/is_block_features_monthly'
                license_type:
                  $ref: '#/components/schemas/Plan/properties/license_type'
                trial_period:
                  $ref: '#/components/schemas/Plan/properties/trial_period'
                is_require_subscription:
                  $ref: '#/components/schemas/Plan/properties/is_require_subscription'
                support_forum:
                  $ref: '#/components/schemas/Plan/properties/support_forum'
                support_kb:
                  $ref: '#/components/schemas/Plan/properties/support_kb'
                support_email:
                  $ref: '#/components/schemas/Plan/properties/support_email'
                support_phone:
                  $ref: '#/components/schemas/Plan/properties/support_phone'
                is_success_manager:
                  $ref: '#/components/schemas/Plan/properties/is_success_manager'
                is_featured:
                  $ref: '#/components/schemas/Plan/properties/is_featured'
              type: object
      responses:
        '200':
          description: 'A new plan is created.'
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Plan'
        '400':
          $ref: '#/components/responses/400'
        '401':
          $ref: '#/components/responses/401'
        '402':
          $ref: '#/components/responses/402'
        '404':
          $ref: '#/components/responses/404'
      security:
        -
          ApiAuthFSACookie: []
        -
          ApiAuthFSAHeader: []
      x-remove-from-doc: true
      x-internal: true
    parameters:
      -
        $ref: '#/components/parameters/developer_id'
      -
        $ref: '#/components/parameters/product_id'
  '/products/{product_id}/plans/{plan_id}/pricing/clone.json':
    post:
      tags:
        - Plans
      summary: 'Clone pricing to other currency'
      description: 'Create new pricing in a specified currency from an existing one.'
      operationId: plans/clone-pricing-other-currency
      requestBody:
        required: true
        content:
          application/json:
            schema:
              properties:
                to_currency:
                  description: 'The currency of the pricing to be created.'
                  type: string
                  enum: [eur, usd, gbp]
                  example: eur
                from_currency:
                  description: 'The currency of the pricing to clone.'
                  type: string
                  default: usd
                  enum: [eur, usd, gbp]
              type: object
      responses:
        '201':
          description: 'New pricing for the currency created.'
          content:
            application/json:
              schema:
                properties:
                  pricing: { type: array, items: { $ref: '#/components/schemas/Pricing' } }
                type: object
        '400':
          $ref: '#/components/responses/400'
        '401':
          $ref: '#/components/responses/401'
        '402':
          $ref: '#/components/responses/402'
        '404':
          $ref: '#/components/responses/404'
    parameters:
      -
        $ref: '#/components/parameters/product_id'
      -
        $ref: '#/components/parameters/plan_id'
  '/products/{product_id}/plans/{plan_id}/pricing/{pricing_id}.json':
    get:
      tags:
        - Plans
      summary: 'Retrieve a pricing'
      description: 'Retrieve a specific plan pricing by ID.'
      operationId: plans/retrieve-pricing
      parameters:
        -
          $ref: '#/components/parameters/fields'
      responses:
        '200':
          description: 'The plan pricing.'
          content:
            application/json:
              schema:
                properties:
                  pricing: { $ref: '#/components/schemas/Pricing' }
                type: object
        '400':
          $ref: '#/components/responses/400'
        '401':
          $ref: '#/components/responses/401'
        '402':
          $ref: '#/components/responses/402'
        '404':
          $ref: '#/components/responses/404'
    parameters:
      -
        $ref: '#/components/parameters/product_id'
      -
        $ref: '#/components/parameters/plan_id'
      -
        $ref: '#/components/parameters/pricing_id'
  '/developers/{developer_id}/products/{product_id}/plans/{plan_id}/pricing/{pricing_id}.json':
    put:
      tags:
        - Plans
      summary: 'Update a pricing'
      description: "Update the plan's pricing by ID.\n\n> Only developers can update a plan pricing."
      operationId: plans/update-pricing
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/Pricing'
      responses:
        '200':
          description: 'The plan pricing was updated.'
          content:
            application/json:
              schema:
                properties:
                  pricing: { $ref: '#/components/schemas/Pricing' }
                type: object
        '400':
          $ref: '#/components/responses/400'
        '401':
          $ref: '#/components/responses/401'
        '402':
          $ref: '#/components/responses/402'
        '404':
          $ref: '#/components/responses/404'
      security:
        -
          ApiAuthFSACookie: []
        -
          ApiAuthFSAHeader: []
      x-remove-from-doc: true
      x-internal: true
    delete:
      tags:
        - Plans
      summary: 'Delete a plan''s pricing'
      description: "Delete the plan pricing by ID.\n\n> Only developers can delete a plan pricing."
      operationId: plans/delete-s-pricing
      responses:
        '204':
          description: 'The plan pricing was deleted.'
        '400':
          $ref: '#/components/responses/400'
        '401':
          $ref: '#/components/responses/401'
        '402':
          $ref: '#/components/responses/402'
        '404':
          $ref: '#/components/responses/404'
      security:
        -
          ApiAuthFSACookie: []
        -
          ApiAuthFSAHeader: []
      x-remove-from-doc: true
      x-internal: true
    parameters:
      -
        $ref: '#/components/parameters/developer_id'
      -
        $ref: '#/components/parameters/product_id'
      -
        $ref: '#/components/parameters/plan_id'
      -
        $ref: '#/components/parameters/pricing_id'
  '/products/{product_id}/plans/{plan_id}/pricing.json':
    get:
      tags:
        - Plans
      summary: 'List all plan''s pricing'
      description: 'Retrieve the collection of all the plan''s pricings.'
      operationId: plans/list-s-pricing
      parameters:
        -
          $ref: '#/components/parameters/fields'
        -
          name: currency
          in: query
          schema:
            $ref: '#/components/schemas/CommonEnums/properties/Currency'
        -
          $ref: '#/components/parameters/count'
        -
          $ref: '#/components/parameters/offset'
      responses:
        '200':
          description: 'The collection of the plan''s pricing.'
          content:
            application/json:
              schema:
                properties:
                  pricing: { type: array, items: { $ref: '#/components/schemas/Pricing' } }
                type: object
        '400':
          $ref: '#/components/responses/400'
        '401':
          $ref: '#/components/responses/401'
        '402':
          $ref: '#/components/responses/402'
        '404':
          $ref: '#/components/responses/404'
    parameters:
      -
        $ref: '#/components/parameters/product_id'
      -
        $ref: '#/components/parameters/plan_id'
  '/developers/{developer_id}/products/{product_id}/plans/{plan_id}/pricing.json':
    post:
      tags:
        - Plans
      summary: 'Create a pricing'
      description: 'Create new pricing for a plan.'
      operationId: plans/create-pricing
      parameters:
        -
          $ref: '#/components/parameters/fields'
        -
          name: currency
          in: query
          schema:
            $ref: '#/components/schemas/CommonEnums/properties/Currency'
      requestBody:
        required: true
        content:
          application/json:
            schema:
              properties:
                monthly_price:
                  $ref: '#/components/schemas/Pricing/properties/monthly_price'
                annual_price:
                  $ref: '#/components/schemas/Pricing/properties/annual_price'
                lifetime_price:
                  $ref: '#/components/schemas/Pricing/properties/lifetime_price'
                licenses:
                  $ref: '#/components/schemas/Pricing/properties/licenses'
                currency: {  }
              type: object
      responses:
        '200':
          description: 'The pricing for the plan has been created.'
          content:
            application/json:
              schema:
                properties:
                  pricing: { $ref: '#/components/schemas/Pricing' }
                type: object
        '400':
          $ref: '#/components/responses/400'
        '401':
          $ref: '#/components/responses/401'
        '402':
          $ref: '#/components/responses/402'
        '404':
          $ref: '#/components/responses/404'
      security:
        -
          ApiAuthFSACookie: []
        -
          ApiAuthFSAHeader: []
      x-remove-from-doc: true
      x-internal: true
    parameters:
      -
        $ref: '#/components/parameters/product_id'
      -
        $ref: '#/components/parameters/plan_id'
  '/products/{product_id}/plans/{plan_id}/pricing/{pricing_id}/licenses.json':
    post:
      tags:
        - Plans
      summary: 'Create a license'
      description: "Create a new license for the plan and pricing. Please note that:\n1. Either `period` or `expires_at` or `is_block_features` must be set.\n2. If you create a license with `is_block_features` set to `false` and do not specify `period` and `expires_at`, the license will never expire or block features and will continue to work for lifetime.\n3. If you specify an email address, the user must have already activated a license or installed your product before. If your user has not activated a license, then please don't use the field and when they activate the license we will collect their email and register the user with Freemius.\n4. Use the `source` parameter only when creating migrated licenses from a legacy system.\n\nMore information about every other parameters can be found below.\n"
      operationId: plans/create-license
      requestBody:
        required: true
        content:
          application/json:
            schema:
              properties:
                is_whitelabeled:
                  $ref: '#/components/schemas/License/properties/is_whitelabeled'
                period:
                  $ref: '#/components/schemas/Subscription/properties/billing_cycle'
                is_block_features:
                  $ref: '#/components/schemas/License/properties/is_block_features'
                expires_at:
                  $ref: '#/components/schemas/License/properties/expiration'
                email:
                  description: '(optional) License owner email.'
                  type: string
                existing_install_id:
                  description: '(optional) If the module type is `bundle` and `existing_install_id` is a valid ID of an install that is using a product of the bundle, a child license will automatically be created and activated for the install.'
                  type: string
                send_email:
                  description: '(optional) Whether to email the license key and download link to the user.'
                  type: boolean
                source:
                  $ref: '#/components/schemas/License/properties/source'
                license_key:
                  description: '(optional) Predefined license key - this can be used when duplicating a license of another product into another product.'
                  type: string
              type: object
      responses:
        '200':
          description: 'The license created successfully.'
          content:
            application/json:
              schema:
                properties:
                  license: { $ref: '#/components/schemas/License' }
                type: object
    parameters:
      -
        $ref: '#/components/parameters/product_id'
      -
        $ref: '#/components/parameters/plan_id'
      -
        $ref: '#/components/parameters/pricing_id'
  '/products/{product_id}/portal/login.json':
    post:
      tags:
        - Products
      summary: 'Generate portal login link'
      description: 'Generate a direct login link for a user in the context of the store of the product. The login link is valid for 5 minutes from generation. Either user ID or email must be provided.'
      operationId: products/generate-portal-login-link
      requestBody:
        required: true
        content:
          application/json:
            schema:
              properties:
                id:
                  description: 'The ID of the user. Either id or email is required.'
                  type: string
                  format: int64
                  minimum: 0
                email:
                  description: 'The email of the user. Either id or email is required.'
                  type: string
                  format: email
              type: object
      responses:
        '201':
          description: 'Portal login link generated successfully.'
          content:
            application/json:
              schema:
                properties:
                  token: { description: 'The generated portal session token.', type: string }
                  link: { description: 'The complete portal login URL with the token.', type: string, format: uri }
                type: object
        '400':
          $ref: '#/components/responses/400'
        '404':
          $ref: '#/components/responses/404'
    parameters:
      -
        $ref: '#/components/parameters/product_id'
  '/products/{product_id}/pricing.json':
    get:
      tags:
        - Products
      summary: 'Retrieve the pricing table data'
      description: 'Retrieve the plugin''s full features & pricing data for a pricing table. Used by our [JS SDK](help-documentation-saas-sdk-react-starter-components.md#subscription-plans-table), and [WordPress SDK](help-documentation-wordpress-sdk-wp-admin-in-dashboard-upgrading.md) to create pricing components and pages.'
      operationId: products/retrieve-pricing-table-data
      parameters:
        -
          name: currency
          in: query
          description: 'The currency to use for the pricing.'
          required: false
          schema:
            $ref: '#/components/schemas/CommonEnums/properties/Currency'
        -
          name: show_pending
          in: query
          description: ''
          required: false
          schema:
            type: boolean
            default: false
        -
          name: type
          in: query
          description: 'Whether to show all plans or only the visible ones.'
          required: false
          schema:
            default: all
            enum:
              - all
              - visible
        -
          name: is_enriched
          in: query
          description: 'If set to `true`, the result will be enriched with some of the context plugin''s information.'
          required: false
          schema:
            type: boolean
            default: false
        -
          name: bundle_product_id
          in: query
          description: '(optional) (Development Only) The ID of the parent bundle product. When getting the pricing of a product, if the product is part of a bundle, you can set the value here (along with the public key of the bundle). This will be used to determine the trial status of the product in sandbox mode. Our WP SDK uses it internally.'
          required: false
          schema:
            type: string
        -
          name: bundle_product_public_key
          in: query
          description: '(optional) (Development Only) Used alongside the `bundle_product_id` parameter.'
          required: false
          schema:
            type: string
      responses:
        '200':
          description: 'The features and pricing data.'
          content:
            application/json:
              schema:
                properties:
                  plugin: { properties: { icon: { $ref: '#/components/schemas/Plugin/properties/icon' }, slug: { $ref: '#/components/schemas/Plugin/properties/slug' }, title: { $ref: '#/components/schemas/Plugin/properties/title' }, type: { $ref: '#/components/schemas/Plugin/properties/type' }, money_back_period: { $ref: '#/components/schemas/Plugin/properties/money_back_period' }, refund_policy: { $ref: '#/components/schemas/Plugin/properties/refund_policy' }, public_key: { $ref: '#/components/schemas/Plugin/properties/public_key' }, parent_plugin_id: { $ref: '#/components/schemas/Plugin/properties/parent_plugin_id' }, selling_unit_label: { description: 'The label used for the selling unit of the product, e.g., ''Credit'', ''Activation'', etc. The resulting object will have both singular and plural.', properties: { singular: { description: 'The singular form of the selling unit label.', type: string, example: Credit }, plural: { description: 'The plural form of the selling unit label.', type: string, example: Credits } }, type: object, nullable: false } }, type: object, nullable: false }
                  plans: { type: array, items: { allOf: [{ $ref: '#/components/schemas/Plan' }, { properties: { pricing: { type: array, items: { $ref: '#/components/schemas/Pricing' } } }, type: object }, { properties: { features: { type: array, items: { $ref: '#/components/schemas/FeatureEnriched' } } }, type: object }] }, nullable: false }
                  reviews: { description: 'Verified and featured reviews of the product.', type: array, items: { $ref: '#/components/schemas/PluginReview' } }
                  active_installs: { description: 'The estimated number of active installs of the product.', type: integer, example: 10000 }
                  downloads: { description: 'The estimated number of downloads of the product.', type: integer, example: 5000 }
                  all_plans_single_site_pricing: { description: 'Single site pricing for all plans indexed by plan ID', type: object, example: { '16633': { monthly_price: { usd: 9.99, gbp: 7.99, eur: 8.99 }, annual_price: { usd: 99.99, gbp: 79.99, eur: 89.99 }, lifetime_price: { usd: 299.99, gbp: 249.99, eur: 279.99 } } }, additionalProperties: { schema: FSEndpointDeveloperPluginPricing, description: 'The key represents the ID of the plan', properties: { monthly_price: { description: 'Monthly pricing in different currencies', properties: { usd: { type: number, format: float, example: 9.99 }, gbp: { type: number, format: float, example: 7.99 }, eur: { type: number, format: float, example: 8.99 } }, type: object }, annual_price: { description: 'Annual pricing in different currencies', properties: { usd: { type: number, format: float, example: 99.99 }, gbp: { type: number, format: float, example: 79.99 }, eur: { type: number, format: float, example: 89.99 } }, type: object }, lifetime_price: { description: 'Lifetime pricing in different currencies', properties: { usd: { type: number, format: float, example: 299.99 }, gbp: { type: number, format: float, example: 249.99 }, eur: { type: number, format: float, example: 279.99 } }, type: object } }, type: object } }
                  checkout_url: { description: 'The URL to the Freemius Checkout. You need to append the product id and plan id as necessary. Please refer to the [Checkout documentation](help-documentation-selling-with-freemius-hosted-checkout.md) for more information.', type: string, example: 'https://checkout.freemius.com' }
                  fs_wp_endpoint_url: { description: 'The URL to the Freemius WP Endpoint. This is internally used by the Freemius SDK.', type: string, example: 'https://wp.freemius.com' }
                  trial_mode: { description: 'Whenther the product supports trial for the current install/site. This is relevant for WP products only.', type: boolean, example: true }
                  trial_utilized: { description: 'Whether the trial has been utilized for the current install/site. This is relevant for WP products only.', type: boolean, example: false }
                type: object
        '400':
          $ref: '#/components/responses/400'
        '401':
          $ref: '#/components/responses/401'
        '402':
          $ref: '#/components/responses/402'
        '404':
          $ref: '#/components/responses/404'
    parameters:
      -
        $ref: '#/components/parameters/product_id'
  '/products/{product_id}/reviews/{review_id}.json':
    get:
      tags:
        - Reviews
      summary: 'Retrieve a review'
      description: 'Retrieve a product review by ID.'
      operationId: reviews/retrieve
      responses:
        '200':
          description: 'The retrieved review.'
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/PluginReview'
        '400':
          $ref: '#/components/responses/400'
        '401':
          $ref: '#/components/responses/401'
        '402':
          $ref: '#/components/responses/402'
        '404':
          $ref: '#/components/responses/404'
    put:
      tags:
        - Reviews
      summary: 'Update a review'
      description: "Update a product review by ID\n> The rate can only be modified for developer generated reviews."
      operationId: reviews/update
      parameters:
        -
          $ref: '#/components/parameters/fields'
      requestBody:
        required: true
        content:
          multipart/form-data:
            schema:
              properties:
                picture:
                  description: 'Reviewer''s profile picture. A maximum of 200KB in size and 300px width and 300px height is allowed.'
                  type: string
                  format: binary
                data:
                  $ref: '#/components/schemas/CommonRequestSchemas/properties/MultipartJsonData'
              type: object
          application/json:
            schema:
              properties:
                title:
                  $ref: '#/components/schemas/PluginReview/properties/title'
                text:
                  $ref: '#/components/schemas/PluginReview/properties/text'
                name:
                  $ref: '#/components/schemas/PluginReview/properties/name'
                rate:
                  $ref: '#/components/schemas/PluginReview/properties/rate'
                job_title:
                  $ref: '#/components/schemas/PluginReview/properties/job_title'
                company:
                  $ref: '#/components/schemas/PluginReview/properties/company'
                company_url:
                  $ref: '#/components/schemas/PluginReview/properties/company_url'
                profile_url:
                  $ref: '#/components/schemas/PluginReview/properties/profile_url'
                is_featured:
                  $ref: '#/components/schemas/PluginReview/properties/is_featured'
              type: object
      responses:
        '200':
          description: 'The updated review.'
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/PluginReview'
        '400':
          $ref: '#/components/responses/400'
        '401':
          $ref: '#/components/responses/401'
        '402':
          $ref: '#/components/responses/402'
        '404':
          $ref: '#/components/responses/404'
    delete:
      tags:
        - Reviews
      summary: 'Delete a review'
      description: 'Delete a product review by ID.'
      operationId: reviews/delete
      responses:
        '204':
          $ref: '#/components/responses/204'
        '400':
          $ref: '#/components/responses/400'
        '401':
          $ref: '#/components/responses/401'
        '402':
          $ref: '#/components/responses/402'
        '404':
          $ref: '#/components/responses/404'
    parameters:
      -
        $ref: '#/components/parameters/product_id'
      -
        $ref: '#/components/parameters/review_id'
  '/products/{product_id}/reviews.json':
    get:
      tags:
        - Reviews
      summary: 'List all reviews'
      description: 'Retrieve the reviews collection.'
      operationId: reviews/list
      responses:
        '200':
          description: 'The reviews collection.'
          content:
            application/json:
              schema:
                properties:
                  reviews: { type: array, items: { $ref: '#/components/schemas/PluginReview' } }
                type: object
        '400':
          $ref: '#/components/responses/400'
        '401':
          $ref: '#/components/responses/401'
        '402':
          $ref: '#/components/responses/402'
        '404':
          $ref: '#/components/responses/404'
    post:
      tags:
        - Reviews
      summary: 'Create a review'
      description: 'Create a product review.'
      operationId: reviews/create
      requestBody:
        required: true
        content:
          multipart/form-data:
            schema:
              properties:
                picture:
                  description: 'Reviewer''s profile picture. A maximum of 200KB in size and 300px width and 300px height is allowed.'
                  type: string
                  format: binary
                data:
                  $ref: '#/components/schemas/CommonRequestSchemas/properties/MultipartJsonData'
              type: object
          application/json:
            schema:
              properties:
                title:
                  $ref: '#/components/schemas/PluginReview/properties/title'
                text:
                  $ref: '#/components/schemas/PluginReview/properties/text'
                name:
                  $ref: '#/components/schemas/PluginReview/properties/name'
                rate:
                  $ref: '#/components/schemas/PluginReview/properties/rate'
                job_title:
                  $ref: '#/components/schemas/PluginReview/properties/job_title'
                company:
                  $ref: '#/components/schemas/PluginReview/properties/company'
                company_url:
                  $ref: '#/components/schemas/PluginReview/properties/company_url'
                profile_url:
                  $ref: '#/components/schemas/PluginReview/properties/profile_url'
                is_featured:
                  $ref: '#/components/schemas/PluginReview/properties/is_featured'
                is_active:
                  description: 'Whether the review is active or not.'
                  type: boolean
                  default: 'true'
              type: object
      responses:
        '200':
          description: 'The retrieved review.'
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/PluginReview'
        '400':
          $ref: '#/components/responses/400'
        '401':
          $ref: '#/components/responses/401'
        '402':
          $ref: '#/components/responses/402'
        '404':
          $ref: '#/components/responses/404'
    parameters:
      -
        $ref: '#/components/parameters/product_id'
  '/products/{product_id}/reviews/summary.json':
    get:
      tags:
        - Reviews
      summary: 'Retrieve reviews summary'
      description: 'Retrieve the summary of the reviews collection. Every item is an object with a `rate` and `count` properties, where `rate` is the rating value (0-100) and `count` is the number of reviews with that rating. Reviews are grouped by their rating.'
      operationId: reviews/retrieve-summary
      parameters:
        -
          name: type
          in: query
          schema:
            description: '(Optional) Whether to retrieve only verified reviews or both verified and unverified reviews.'
            type: string
            default: verified
            enum:
              - all
              - verified
      responses:
        '200':
          description: 'The summary of the review collection.'
          content:
            application/json:
              schema:
                properties:
                  reviews: { type: array, items: { properties: { rate: { $ref: '#/components/schemas/PluginReview/properties/rate' }, count: { description: 'The total number of reviews that have the same rating for the product.', type: string, format: int64, minimum: 1, example: '10', nullable: false } }, type: object } }
                type: object
        '400':
          $ref: '#/components/responses/400'
        '401':
          $ref: '#/components/responses/401'
        '402':
          $ref: '#/components/responses/402'
        '404':
          $ref: '#/components/responses/404'
    parameters:
      -
        $ref: '#/components/parameters/product_id'
  '/products/{product_id}/settings/{setting_id}.json':
    get:
      tags:
        - Products
      summary: 'Retrieve a setting'
      description: "Retrieve a specific product setting.\n > Different settings are used for different functionalities around product. Please use the Developer Dashboard instead to modify the functionality."
      operationId: products/retrieve-setting
      parameters:
        -
          $ref: '#/components/parameters/fields'
      responses:
        '200':
          description: 'The product setting.'
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Setting'
        '400':
          $ref: '#/components/responses/400'
        '401':
          $ref: '#/components/responses/401'
        '402':
          $ref: '#/components/responses/402'
        '404':
          $ref: '#/components/responses/404'
      x-remove-from-doc: true
      x-internal: true
    put:
      tags:
        - Products
      summary: 'Update a setting'
      description: "Update a specific product setting.\n > Different settings are used for different functionalities around product. Please use the Developer Dashboard instead to modify the functionality."
      operationId: products/update-setting
      parameters:
        -
          $ref: '#/components/parameters/fields'
      requestBody:
        content:
          application/json:
            schema:
              properties:
                data:
                  $ref: '#/components/schemas/Setting/properties/data'
              type: object
      responses:
        '200':
          description: 'Updated product settings.'
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Setting'
        '400':
          $ref: '#/components/responses/400'
        '401':
          $ref: '#/components/responses/401'
        '402':
          $ref: '#/components/responses/402'
        '404':
          $ref: '#/components/responses/404'
      x-remove-from-doc: true
      x-internal: true
    delete:
      tags:
        - Products
      summary: 'Delete a setting'
      description: 'Delete a specific product setting.'
      operationId: products/delete-setting
      responses:
        '204':
          $ref: '#/components/responses/204'
        '400':
          $ref: '#/components/responses/400'
        '401':
          $ref: '#/components/responses/401'
        '402':
          $ref: '#/components/responses/402'
        '404':
          $ref: '#/components/responses/404'
      x-remove-from-doc: true
      x-internal: true
    parameters:
      -
        $ref: '#/components/parameters/product_id'
      -
        $ref: '#/components/parameters/setting_id'
  '/products/{product_id}/skip.json':
    put:
      tags:
        - Products
      summary: 'Skip account connection'
      description: 'Skip the account connection step for the specified product. This is useful for testing purposes or for WordPress product integration. The functionality is handled automatically by our [WordPress SDK](https://github.com/Freemius/wordpress-sdk).'
      operationId: products/skip-account-connection
      requestBody:
        required: true
        content:
          application/json:
            schema:
              properties:
                uids:
                  description: 'MD5 Collection of unique site identifiers.'
                  type: array
                  items: { $ref: '#/components/schemas/CommonProperties/properties/uid' }
                uid:
                  $ref: '#/components/schemas/CommonProperties/properties/uid'
              type: object
      responses:
        '204':
          $ref: '#/components/responses/204'
        '400':
          $ref: '#/components/responses/400'
        '401':
          $ref: '#/components/responses/401'
        '402':
          $ref: '#/components/responses/402'
        '404':
          $ref: '#/components/responses/404'
      x-remove-from-doc: true
      x-internal: true
    parameters:
      -
        $ref: '#/components/parameters/product_id'
  '/products/{product_id}/subscriptions/{subscription_id}.json':
    get:
      tags:
        - Subscriptions
      summary: 'Retrieve a subscription'
      description: 'Retrieve a subscription associated with your product.'
      operationId: subscriptions/retrieve
      parameters:
        -
          $ref: '#/components/parameters/fields'
      responses:
        '200':
          description: 'Subscription retrieved.'
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Subscription'
        '401':
          $ref: '#/components/responses/401'
        '402':
          $ref: '#/components/responses/402'
        '404':
          $ref: '#/components/responses/404'
    put:
      tags:
        - Subscriptions
      summary: 'Update a subscription'
      description: 'Update a subscription to activate a cancellation coupon.'
      operationId: subscriptions/update
      requestBody:
        required: true
        content:
          application/json:
            schema:
              properties:
                coupon_id:
                  description: 'The subscription cancellation coupon ID. The coupon must be set as a special "Cancellation Coupon" in the Freemius Developer Dashboard. The discount will be applied to the next renewals.'
                  type: integer
                  nullable: false
              type: object
      responses:
        '200':
          description: 'Subscription retrieved.'
          content:
            application/json:
              schema:
                allOf:
                  - { $ref: '#/components/schemas/Subscription' }
                  - { properties: { has_subscription_cancellation_discount: { description: 'Shows whether a subscription cancellation discount was applied to the subscription.', type: boolean, example: false, nullable: true } }, type: object }
        '401':
          $ref: '#/components/responses/401'
        '402':
          $ref: '#/components/responses/402'
        '404':
          $ref: '#/components/responses/404'
    delete:
      tags:
        - Subscriptions
      summary: 'Cancel a subscription'
      description: "Use this endpoint to **cancel the subscription**. If the subscription is currently in a **trialing state**, this will also cancel the trial.\n\nThis is useful when you want to programmatically offer a cancellation feature from within your SaaS or custom dashboards. If you're integrating Freemius with your SaaS, please see our [guide here](help-documentation-selling-with-freemius-saas-integration.md).\n\n> ⚠️ This action is irreversible and will immediately cancel the subscription or trial.\n\nCancelling an already cancelled subscription will not have any effect and the endpoint will return the same subscription details as before."
      operationId: subscriptions/cancel
      parameters:
        -
          name: reason_ids
          in: query
          description: 'Optional cancellation reason IDs.'
          schema:
            type: array
            items:
              $ref: '#/components/schemas/Uninstall/properties/reason_id'
        -
          parameter: reason
          name: reason
          in: query
          schema:
            $ref: '#/components/schemas/Uninstall/properties/reason_info'
      responses:
        '200':
          description: 'Subscription retrieved.'
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Subscription'
        '401':
          $ref: '#/components/responses/401'
        '402':
          $ref: '#/components/responses/402'
        '404':
          $ref: '#/components/responses/404'
    parameters:
      -
        $ref: '#/components/parameters/product_id'
      -
        $ref: '#/components/parameters/subscription_id'
  '/products/{product_id}/subscriptions.json':
    get:
      tags:
        - Subscriptions
      summary: 'List all subscriptions'
      description: "Retrieve the subscription collecttion associated with your product.\n> Subscriptions are created when someone purchases your product using the [Freemius Checkout](checkout.md).\n\n### Searching and filtering\nThere are various parameters to help you search and/or filter subscription.\n- You can search by subscription ID, external subscription ID, or user email.\n- You can also filter by billing cycle, gateway, plan ID, and subscription status.\nPlease see the parameters for more information."
      operationId: subscriptions/list
      parameters:
        -
          name: search
          in: query
          description: 'Optional search: subscription id, external subscription id or user email'
          schema:
            type: string
        -
          $ref: '#/components/parameters/billing_cycle'
        -
          $ref: '#/components/parameters/gateway'
        -
          name: filter
          in: query
          description: 'Optional filtering based on the status of the subscription. Defaults to `all`.'
          schema:
            type: string
            default: all
            enum:
              - all
              - active
              - cancelled
        -
          name: extended
          in: query
          description: 'When set to `true` enrich the subscriptions with the plan name, install URL & title, and user email.'
          schema:
            type: boolean
            example: 'false'
        -
          name: enrich_with_cancellation_discounts
          in: query
          description: 'When set to `true` enrich the subscription to include any cancellation discounts applied to the subscriptions.'
          schema:
            type: boolean
            example: 'false'
        -
          $ref: '#/components/parameters/count'
        -
          $ref: '#/components/parameters/offset'
        -
          $ref: '#/components/parameters/fields'
        -
          name: sort
          in: query
          description: 'The sort order of the subscriptions. Example: -id. Default: -id.'
          schema:
            type: string
            enum:
              - id
              - next_payment
            example: '-id'
      responses:
        '200':
          description: 'Provides a collection of subscriptions associated with the product. All subscriptions are listed under the `subscriptions` key.'
          content:
            application/json:
              schema:
                properties:
                  subscriptions: { type: array, items: { allOf: [{ $ref: '#/components/schemas/Subscription' }, { properties: { plan_name: { description: 'Name of the plan associated with the subscription. (Only available when `extended` is set to `true`.)', type: string, example: Professional, nullable: true }, email: { description: 'Email of the user associated with the subscription. (Only available when `extended` is set to `true`.)', type: string, example: foo@freemius.com, nullable: true }, url: { description: 'URL of the installation associated with the subscription. (Only available when `extended` is set to `true`.)', type: string, example: 'https://example.com', nullable: true }, title: { description: 'Title of the installation associated with the subscription. (Only available when `extended` is set to `true`.)', type: string, example: 'Website title', nullable: true }, has_subscription_cancellation_discount: { description: 'Whether subscription cancellation discount was already applied. (Only available when `enrich_with_cancellation_discounts` is set to `true`.)', type: boolean, example: true, nullable: true } }, type: object }] } }
                  discounts: { description: 'The key represents the ID of the subscription', additionalProperties: { schema: FSEndpointDeveloperPluginSubscriptions, type: array, items: { $ref: '#/components/schemas/Discount' } } }
                type: object
        '400':
          $ref: '#/components/responses/400'
        '401':
          $ref: '#/components/responses/401'
        '402':
          $ref: '#/components/responses/402'
        '404':
          $ref: '#/components/responses/404'
    parameters:
      -
        $ref: '#/components/parameters/product_id'
  '/products/{product_id}/subscriptions/{subscription_id}/payments.json':
    get:
      tags:
        - Subscriptions
      summary: 'List all payments'
      description: 'Retrieve the payment collection associated with the subscription.'
      operationId: subscriptions/list-payments
      parameters:
        -
          $ref: '#/components/parameters/count'
        -
          $ref: '#/components/parameters/offset'
        -
          $ref: '#/components/parameters/fields'
      responses:
        '200':
          description: 'Provides a collection of payments associated with the subscription. All payments are listed under the `payments` key.'
          content:
            application/json:
              schema:
                properties:
                  payments: { type: array, items: { $ref: '#/components/schemas/Payment' } }
                type: object
        '400':
          $ref: '#/components/responses/400'
        '401':
          $ref: '#/components/responses/401'
        '402':
          $ref: '#/components/responses/402'
        '404':
          $ref: '#/components/responses/404'
    post:
      tags:
        - Subscriptions
      summary: 'Create a new migrated payment'
      description: 'In case you want to synchronize migrated subscription from the legacy platform use this endpoint to have our system log a migrated payment. Depending on your use case you can also choose to extend the license. Please read our [migration documentation](help-documentation-migration.md) to learn more.'
      operationId: subscriptions/create-new-migrated-payment
      requestBody:
        required: true
        content:
          application/json:
            schema:
              properties:
                gross:
                  $ref: '#/components/schemas/Payment/properties/gross'
                payment_external_id:
                  $ref: '#/components/schemas/Payment/properties/external_id'
                source:
                  $ref: '#/components/schemas/Migration/properties/source_external_id'
                vat:
                  $ref: '#/components/schemas/Payment/properties/vat'
                gateway_fee:
                  $ref: '#/components/schemas/Payment/properties/gateway_fee'
                processed_at:
                  $ref: '#/components/schemas/Cart/properties/completed'
                is_extend_license:
                  description: 'Whether the license should be extended. The default value is `false`.'
                  type: boolean
                next_payment:
                  $ref: '#/components/schemas/Subscription/properties/next_payment'
              type: object
      responses:
        '200':
          description: 'The payment was successfully created.'
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Payment'
        '400':
          $ref: '#/components/responses/400'
        '401':
          $ref: '#/components/responses/401'
        '402':
          $ref: '#/components/responses/402'
        '404':
          $ref: '#/components/responses/404'
    parameters:
      -
        $ref: '#/components/parameters/product_id'
      -
        $ref: '#/components/parameters/subscription_id'
  '/products/{product_id}/tags/{tag_id}.json':
    put:
      tags:
        - Deployments
      summary: 'Update a deployment'
      description: "Update a specific deployed version of the product. This applies to WordPress products only. Use this endpoint to update the `release_mode` of a deployment to make it available to your customers.\n\n### Release Modes\n\nDefined by the `release_mode` property, with the following possible values:\n\n- `pending` – The deployment is pending and not visible to customers. This is the default value.\n- `beta` – The deployment is in beta mode. Only customers with beta access will see this version.\n- `released` – The deployment is released and visible to all customers.\n\nAdditionally, WordPress plugins and themes support **incremental releases** and **staged rollouts**:\n\n- [**Incremental Release**](help-documentation-release-management-incremental-update.md): Controlled via the `is_incremental` flag, incremental releases enforce sequential updates, requiring users to install designated intermediate versions before proceeding to newer ones.\n- [**Staged Rollout**](help-documentation-release-management-staged-rollouts.md): Managed through the `limit` and `percentage_limit` flags, staged rollouts enable gradual deployment of updates to a subset of users, allowing for monitoring and issue resolution before full release.\n\n> Note: Incremental Release and Staged Rollout are not supported for templates and widgets.\n"
      operationId: deployments/update
      requestBody:
        content:
          application/json:
            schema:
              properties:
                release_mode:
                  $ref: '#/components/schemas/PluginTag/properties/release_mode'
                limit:
                  $ref: '#/components/schemas/PluginTag/properties/limit'
                percentage_limit:
                  description: 'Instead of `limit`, you can use this property to limit the percentage of license owners that will receive an update. The value must be between 0 and 100. Behind the scenes the system will count the current active license owners and convert it into an absolute value.'
                  type: integer
                  maximum: 100
                  minimum: 0
                is_incremental:
                  $ref: '#/components/schemas/PluginTag/properties/is_incremental'
              type: object
      responses:
        '200':
          description: 'The updated deployment.'
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/PluginTag'
        '400':
          $ref: '#/components/responses/400'
        '401':
          $ref: '#/components/responses/401'
        '402':
          $ref: '#/components/responses/402'
        '404':
          $ref: '#/components/responses/404'
    parameters:
      -
        $ref: '#/components/parameters/product_id'
      -
        $ref: '#/components/parameters/tag_id'
  '/products/{product_id}/tags/{tag_id}.zip':
    get:
      tags:
        - Deployments
      summary: 'Download a deployment'
      description: "Download a specific deployed version of the product. This is for WordPress products only (including plugins, themes, templates and widgets). It outputs the zip file of the deployed version.\n\n> You can download both the premium and the free version of the deployment using the `is_premium` flag. This will help you setup automation to deploy Freemius generated free version to WordPress.org repository.\n"
      operationId: deployments/download
      parameters:
        -
          name: is_premium
          in: query
          description: '(Optional) Whether to retrieve a premium version of the product or not. For WordPress products (plugins and themes) only.'
          schema:
            type: boolean
            default: 'true'
      responses:
        '200':
          description: 'The zip file of the deployed version.'
          content:
            application/zip: {  }
        '400':
          $ref: '#/components/responses/400'
        '401':
          $ref: '#/components/responses/401'
        '402':
          $ref: '#/components/responses/402'
        '404':
          $ref: '#/components/responses/404'
    parameters:
      -
        $ref: '#/components/parameters/product_id'
      -
        $ref: '#/components/parameters/tag_id'
  '/products/{product_id}/tags.json':
    get:
      tags:
        - Deployments
      summary: 'List all deployments'
      description: 'Get the product version collection. This is for WordPress products only.'
      operationId: deployments/list
      parameters:
        -
          $ref: '#/components/parameters/count'
        -
          $ref: '#/components/parameters/offset'
        -
          $ref: '#/components/parameters/fields'
      responses:
        '200':
          description: 'The product version collection.'
          content:
            application/json:
              schema:
                properties:
                  tags: { type: array, items: { $ref: '#/components/schemas/PluginTag' } }
                type: object
        '400':
          $ref: '#/components/responses/400'
        '401':
          $ref: '#/components/responses/401'
        '402':
          $ref: '#/components/responses/402'
        '404':
          $ref: '#/components/responses/404'
    post:
      tags:
        - Deployments
      summary: 'Create a deployment'
      description: "Upload a new version of the product (for WordPress products only). The endpoint supports only the `multipart/form-data` content type and expects two payloads: `file` and `data`.\n\n- `file` - The zip file containing the product. For WordPress plugins or themes this must contain the root directory.\n- `data` - Please omit this when deploying WordPress plugins and themes. In case of deploying templates and widgets, this needs to be a **stringified JSON** and must have the `version` and `requires_platform_version` properties.\n\nAn example of the `data` property:\n\n```\n{\"version\": \"2.0.0\", \"requires_platform_version\": \"1.0.0\"}\n```\n\n> After you have created a deployment, please send another PUT request to the newly created version to update the `release_status` to either `released` or `beta`. The default value is `pending` which means none of the customers will be able to see the new version.\n\nYou can learn more about the deployment process [here](https://freemius.com/help/documentation/getting-started/deployment-process/).\n"
      operationId: deployments/create
      requestBody:
        content:
          multipart/form-data:
            schema:
              required:
                - file
              properties:
                file:
                  description: 'The zip file containing the product. For WordPress plugins or themes this must contain the root directory.'
                  type: string
                  format: binary
                data:
                  description: 'The metadata details associated with this specific product version.'
                  type: string
                  format: json
                  example: '{"version": "1.0.0", "requires_platform_version": "1.0.0"}'
              type: object
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/PluginTag'
        '400':
          $ref: '#/components/responses/400'
        '401':
          $ref: '#/components/responses/401'
        '402':
          $ref: '#/components/responses/402'
        '404':
          $ref: '#/components/responses/404'
    parameters:
      -
        $ref: '#/components/parameters/product_id'
  '/products/{product_id}/tags/latest.json':
    get:
      tags:
        - Deployments
      summary: 'Get latest deployment'
      description: 'Get the information about the latest deployment the product has, including a secure download link. The download link will work without any authentication header and will expire in 24 hours.'
      operationId: deployments/get-latest
      parameters:
        -
          name: is_premium
          in: query
          description: '(Optional) Whether to retrieve a premium version of the product or not. For WordPress products (plugins and themes) only.'
          schema:
            type: boolean
            default: 'true'
        -
          name: type
          in: query
          description: 'Type of the latest deployment to load. If the type provided is `all`, the latest `released`, `beta`, or `pending` version will be returned, whichever has the higher version.'
          schema:
            type: string
            default: released
            enum:
              - released
              - beta
              - pending
              - all
      responses:
        '200':
          description: 'The latest deployment information.'
          content:
            application/json:
              schema:
                allOf:
                  - { $ref: '#/components/schemas/PluginTag' }
                  - { properties: { url: { description: 'URL to download the deployed ZIP file. This is a secure URL and does not need any additional authentication header. Will expire after 24 hours from the time of generation.', type: string } }, type: object }
        '400':
          $ref: '#/components/responses/400'
        '401':
          $ref: '#/components/responses/401'
        '402':
          $ref: '#/components/responses/402'
        '404':
          $ref: '#/components/responses/404'
    parameters:
      -
        $ref: '#/components/parameters/product_id'
  '/products/{product_id}/tags/latest.zip':
    get:
      tags:
        - Deployments
      summary: 'Download latest deployment'
      description: 'Download the latest deployment the product has. This is for WordPress products only (including plugins, themes, templates and widgets). It outputs the zip file of the deployed version.'
      operationId: deployments/download-latest
      parameters:
        -
          name: is_premium
          in: query
          description: '(Optional) Whether to retrieve a premium version of the product or not. For WordPress products (plugins and themes) only.'
          schema:
            type: boolean
            default: 'true'
        -
          name: type
          in: query
          description: 'Type of the latest deployment to load. If the type provided is `all`, the latest `released`, `beta`, or `pending` version will be returned, whichever has the higher version.'
          schema:
            type: string
            default: released
            enum:
              - released
              - beta
              - pending
              - all
      responses:
        '200':
          description: 'The zip file of the deployed version.'
          content:
            application/zip: {  }
        '400':
          $ref: '#/components/responses/400'
        '401':
          $ref: '#/components/responses/401'
        '402':
          $ref: '#/components/responses/402'
        '404':
          $ref: '#/components/responses/404'
    parameters:
      -
        $ref: '#/components/parameters/product_id'
  '/products/{product_id}/trials.json':
    get:
      tags:
        - Trials
      summary: 'List all trials'
      description: "List the trial collection associated with the product.\n\nTo support trials, configure your product to [offer trial](help-documentation-selling-with-freemius-free-trials.md) and then users can use the [Freemius Checkout](help-documentation-selling-with-freemius-freemius-checkout-buy-button.md) to start a trial.\n\nYou will need to pass `trial=paid` or `trial=free` to the Checkout's paramters to start a trial."
      operationId: trials/list
      parameters:
        -
          $ref: '#/components/parameters/fields'
        -
          $ref: '#/components/parameters/offset'
        -
          $ref: '#/components/parameters/count'
        -
          $ref: '#/components/parameters/from'
        -
          $ref: '#/components/parameters/to'
      responses:
        '200':
          description: 'Trial collection.'
          content:
            application/json:
              schema:
                properties:
                  trials: { type: array, items: { $ref: '#/components/schemas/Trial' } }
                type: object
        '400':
          $ref: '#/components/responses/400'
        '401':
          $ref: '#/components/responses/401'
        '402':
          $ref: '#/components/responses/402'
        '404':
          $ref: '#/components/responses/404'
    parameters:
      -
        $ref: '#/components/parameters/product_id'
  '/products/{product_id}/uninstall.json':
    put:
      tags:
        - Installations
      summary: 'Uninstall from anonymous site'
      description: 'Uninstall a product from anonymous site'
      operationId: installations/uninstall-from-anonymous-site
      requestBody:
        required: true
        content:
          application/json:
            schema:
              properties:
                uid:
                  $ref: '#/components/schemas/CommonProperties/properties/uid'
                reason_id:
                  $ref: '#/components/schemas/Uninstall/properties/reason_id'
                reason:
                  $ref: '#/components/schemas/Uninstall/properties/reason_info'
              type: object
      responses:
        '200':
          description: 'The product is uninstalled.'
          content:
            application/json:
              schema:
                type: string
              example: '200 OK'
        '400':
          $ref: '#/components/responses/400'
        '401':
          $ref: '#/components/responses/401'
        '402':
          $ref: '#/components/responses/402'
        '404':
          $ref: '#/components/responses/404'
      x-remove-from-doc: true
      x-internal: true
    parameters:
      -
        $ref: '#/components/parameters/product_id'
  '/products/{product_id}/users/{user_id}/billing.json':
    get:
      tags:
        - Users
      summary: 'Retrieve billing'
      description: 'Retrieves the billing information of a user for a specific product.'
      operationId: users/retrieve-billing
      parameters:
        -
          $ref: '#/components/parameters/fields'
      responses:
        '200':
          description: 'Billing Information retrieved.'
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Billing'
        '401':
          $ref: '#/components/responses/401'
        '402':
          $ref: '#/components/responses/402'
        '404':
          $ref: '#/components/responses/404'
    put:
      tags:
        - Users
      summary: 'Update or create billing'
      description: 'Update or create the billing information for a user.'
      operationId: users/update-or-create-billing
      parameters:
        -
          $ref: '#/components/parameters/product_id'
        -
          $ref: '#/components/parameters/user_id'
      requestBody:
        required: true
        content:
          application/json:
            schema:
              properties:
                business_name:
                  $ref: '#/components/schemas/Billing/properties/business_name'
                first:
                  $ref: '#/components/schemas/Billing/properties/first'
                last:
                  $ref: '#/components/schemas/Billing/properties/last'
                email:
                  $ref: '#/components/schemas/Billing/properties/email'
                phone:
                  $ref: '#/components/schemas/Billing/properties/phone'
                website:
                  $ref: '#/components/schemas/Billing/properties/website'
                tax_id:
                  $ref: '#/components/schemas/Billing/properties/tax_id'
                address_street:
                  $ref: '#/components/schemas/Billing/properties/address_street'
                address_apt:
                  $ref: '#/components/schemas/Billing/properties/address_apt'
                address_city:
                  $ref: '#/components/schemas/Billing/properties/address_city'
                address_country:
                  $ref: '#/components/schemas/Billing/properties/address_country'
                address_country_code:
                  $ref: '#/components/schemas/Billing/properties/address_country_code'
                address_state:
                  $ref: '#/components/schemas/Billing/properties/address_state'
                address_zip:
                  $ref: '#/components/schemas/Billing/properties/address_zip'
              type: object
      responses:
        '200':
          description: 'Billing information updated.'
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Billing'
        '401':
          $ref: '#/components/responses/401'
        '402':
          $ref: '#/components/responses/402'
        '404':
          $ref: '#/components/responses/404'
    parameters:
      -
        $ref: '#/components/parameters/product_id'
      -
        $ref: '#/components/parameters/user_id'
  '/products/{product_id}/users/{user_id}/events.json':
    get:
      tags:
        - Users
      summary: 'List all events'
      description: 'Retrieve a log of the events for the user associated with the product. Freemius tracks events such as opt-in, license activation, purchase etc. You can use this data for marketing and other automation purposes. More information can be found [here](help-documentation-marketing-automation-events-webhooks.md).'
      operationId: users/list-events
      parameters:
        -
          $ref: '#/components/parameters/fields'
        -
          $ref: '#/components/parameters/count'
        -
          $ref: '#/components/parameters/offset'
      responses:
        '200':
          description: 'The user''s events log.'
          content:
            application/json:
              schema:
                properties:
                  events: { type: array, items: { $ref: '#/components/schemas/EventLog' } }
                type: object
    parameters:
      -
        $ref: '#/components/parameters/product_id'
      -
        $ref: '#/components/parameters/user_id'
  '/products/{product_id}/users/{user_id}.json':
    get:
      tags:
        - Users
      summary: 'Retrieve a user'
      description: 'Retrieve a user associated with your product.'
      operationId: users/retrieve
      parameters:
        -
          $ref: '#/components/parameters/fields'
      responses:
        '200':
          description: 'The product user data.'
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/User'
        '401':
          $ref: '#/components/responses/401'
        '402':
          $ref: '#/components/responses/402'
        '404':
          $ref: '#/components/responses/404'
    put:
      tags:
        - Users
      summary: 'Update a user'
      description: 'Update a user associated with your product.'
      operationId: users/update
      parameters:
        -
          $ref: '#/components/parameters/fields'
      requestBody:
        required: true
        content:
          application/json:
            schema:
              properties:
                name:
                  description: 'The name of the user (Optional).'
                  type: string
                first:
                  $ref: '#/components/schemas/User/properties/first'
                last:
                  $ref: '#/components/schemas/User/properties/last'
                is_marketing_allowed:
                  $ref: '#/components/schemas/User/properties/is_marketing_allowed'
                is_beta:
                  $ref: '#/components/schemas/User/properties/is_beta'
              type: object
      responses:
        '200':
          description: 'The product user updated data.'
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/User'
        '401':
          $ref: '#/components/responses/401'
        '402':
          $ref: '#/components/responses/402'
        '404':
          $ref: '#/components/responses/404'
    parameters:
      -
        $ref: '#/components/parameters/product_id'
      -
        $ref: '#/components/parameters/user_id'
  '/products/{product_id}/users.json':
    get:
      tags:
        - Users
      summary: 'List all users'
      description: "\nGets the user collection associated with a product.\n\n## Filtering\nThere are a few filters that can be applied to the request.\n\n### Search by email\nYou can specify the parameter `email` to filter the users by email. Optionally you can also put a valid email in the `search` parameter.\n\n### Other filtering options\nThe `search` parameter also accepts the following values:\n\n1. User ID (number).\n2. Full or partial name (string).\n3. Full or partial email (string).\n\n## Pagination\nYou can use the combination of `count` and `offset` parameters to paginate the results.\n"
      operationId: users/list
      parameters:
        -
          $ref: '#/components/parameters/fields'
        -
          $ref: '#/components/parameters/count'
        -
          $ref: '#/components/parameters/offset'
        -
          name: email
          in: query
          description: 'Search user by email address.'
          schema:
            type: string
        -
          name: filter
          in: query
          description: 'Filter user by their financial status'
          schema:
            type: string
            enum:
              - all
              - never_paid
              - paid
              - paying
              - beta
        -
          name: search
          in: query
          description: 'Search by user ID, email or name'
          schema:
            type: string
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                properties:
                  users: { type: array, items: { $ref: '#/components/schemas/User' } }
                type: object
        '400':
          $ref: '#/components/responses/400'
        '401':
          $ref: '#/components/responses/401'
        '402':
          $ref: '#/components/responses/402'
        '404':
          $ref: '#/components/responses/404'
    post:
      tags:
        - Users
      summary: 'Create a user'
      description: "Create a new user associated with the product.\n\nThe user will be linked to the product if they already exist in Freemius.\n\n> User can only be created for products with elevated permissions or during data migration.\n\n## Migrating users from other platforms\n\nFreemius allows to migrate your users from other platforms. To do so, you need to set the `is_migration` parameter to `true`. This will prevent any emails from being sent to the users and will not log any events.\nOnce migrated the user can use their existing licenses to activate your product."
      operationId: users/create
      parameters:
        -
          $ref: '#/components/parameters/fields'
      requestBody:
        required: true
        content:
          application/json:
            schema:
              properties:
                email:
                  description: 'Valid email address.'
                  type: string
                  nullable: false
                password:
                  description: 'Valid password. Must have at least 8 characters.'
                  type: string
                  nullable: false
                ip:
                  description: '(optional) IPv4 or IPv6 Address'
                  type: string
                name:
                  description: '(optional) Full name property. If not specified, `first` and `last` must be provided instead.'
                  type: string
                first:
                  description: '(optional) First name. `Required` if no valid `name` was provided.'
                  type: string
                last:
                  description: '(optional) Last name. `Required` if no valid `name` was provided.'
                  type: string
                picture:
                  description: '(optional) Profile picture URL.'
                  type: string
                is_verified:
                  description: '(optional) Tells if person is already verified, defaults to FALSE.'
                  type: boolean
                after_email_confirm_url:
                  description: '(optional) URL address that the user will be auto forwarded to after email confirmation is clicked.'
                  type: string
                send_verification_email:
                  description: '(optional) Defaults to TRUE. If `false`, email verification message will NOT be sent after registration.'
                  type: boolean
                is_marketing_allowed:
                  $ref: '#/components/schemas/User/properties/is_marketing_allowed'
                is_migration:
                  description: '(optional) If `true`, no emails will be sent to users nor events will be logged.'
                  type: boolean
                source:
                  $ref: '#/components/schemas/Migration/properties/source_external_id'
              type: object
      responses:
        '201':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/User'
        '400':
          $ref: '#/components/responses/400'
        '401':
          $ref: '#/components/responses/401'
        '402':
          $ref: '#/components/responses/402'
    parameters:
      -
        $ref: '#/components/parameters/product_id'
  '/products/{product_id}/users/{user_id}/installs.json':
    get:
      tags:
        - Users
      summary: 'List all installs'
      description: "Retrieve the install collection associated with the user.\n\n Various filtering and search parameters are available to narrow down the results."
      operationId: users/list-installs
      parameters:
        -
          name: install_ids
          in: query
          description: 'Comma-separated install IDs list to filter.'
          schema:
            type: string
            format: comma-separated
          example: '1234,2478,2345'
        -
          name: license_id
          in: query
          description: 'License ID filter. If set, return installs that are linked to the specified license.'
          schema:
            type: integer
        -
          name: plan_id
          in: query
          description: 'Plan ID filter. If set, return installs associated with the given plan.'
          schema:
            type: integer
        -
          $ref: '#/components/parameters/count'
        -
          $ref: '#/components/parameters/offset'
        -
          $ref: '#/components/parameters/fields'
      responses:
        '200':
          description: 'Installs collection'
          content:
            application/json:
              schema:
                properties:
                  installs: { type: array, items: { $ref: '#/components/schemas/Install' } }
                type: object
        '400':
          $ref: '#/components/responses/400'
        '401':
          $ref: '#/components/responses/401'
        '402':
          $ref: '#/components/responses/402'
        '404':
          $ref: '#/components/responses/404'
    parameters:
      -
        $ref: '#/components/parameters/product_id'
      -
        $ref: '#/components/parameters/user_id'
  '/products/{product_id}/users/{user_id}/licenses.json':
    get:
      tags:
        - Users
      summary: 'List all licenses'
      description: 'Retrieve the license collection associated with a user.'
      operationId: users/list-licenses
      parameters:
        -
          $ref: '#/components/parameters/fields'
        -
          $ref: '#/components/parameters/offset'
        -
          $ref: '#/components/parameters/count'
        -
          name: license_key
          in: query
          description: 'Retrieve specific license by its key.'
          schema:
            type: string
        -
          name: ids
          in: query
          description: 'Comma-separated license IDs.'
          schema:
            type: string
        -
          name: license_keys
          in: query
          description: 'Retrieve specific multiple license with a comma-separated string of their license keys.'
          schema:
            type: string
        -
          name: type
          in: query
          description: 'The type of license.'
          schema:
            type: string
            default: all
            enum:
              - all
              - active
              - expired
        -
          $ref: '#/components/schemas/Migration/properties/source'
        -
          name: is_enriched
          in: query
          description: 'Returns the license''s product type.'
          schema:
            type: boolean
            default: false
      responses:
        '200':
          description: 'License collection.'
          content:
            application/json:
              schema:
                properties:
                  licenses: { type: array, items: { allOf: [{ $ref: '#/components/schemas/License' }, { properties: { plugin_type: { description: 'The product type of the license.', type: string }, products: { description: 'List of IDs of children products in case the product is a bundle.', type: array, items: { $ref: '#/components/schemas/Plugin/properties/id' } } }, type: object }] } }
                type: object
        '401':
          $ref: '#/components/responses/401'
        '402':
          $ref: '#/components/responses/402'
        '404':
          $ref: '#/components/responses/404'
    parameters:
      -
        $ref: '#/components/parameters/product_id'
      -
        $ref: '#/components/parameters/user_id'
  '/products/{product_id}/users/{user_id}/licenses/{license_id}/review_url.json':
    get:
      tags:
        - Licenses
      summary: 'Get review URL'
      description: 'Retrieve the review URL associated with a license.'
      operationId: licenses/get-review-url
      responses:
        '200':
          description: 'The retrieved review URL.'
          content:
            application/json:
              schema: {  }
        '400':
          $ref: '#/components/responses/400'
        '401':
          $ref: '#/components/responses/401'
        '402':
          $ref: '#/components/responses/402'
        '404':
          $ref: '#/components/responses/404'
    parameters:
      -
        $ref: '#/components/parameters/product_id'
      -
        $ref: '#/components/parameters/user_id'
      -
        $ref: '#/components/parameters/license_id'
  '/products/{product_id}/users/{user_id}/licenses/{license_id}/reviews.json':
    post:
      tags:
        - Licenses
      summary: 'Create a review'
      description: 'Create a review associated with a license. If you want to create/import reviews which are not associated with a license or from a different system, please use the Review endpoint under `products/{product_id}/reviews.json`.'
      operationId: licenses/create-review
      parameters:
        -
          $ref: '#/components/parameters/fields'
      requestBody:
        description: 'Data needed to create a review with an optional picture. When sending `multipart/form-data` the `data` property must be a JSON object with same structure as the JSON payload.'
        required: true
        content:
          multipart/form-data:
            schema:
              properties:
                picture:
                  description: 'Reviewer''s profile picture. A maximum of 200KB in size and 300px width and 300px height is allowed.'
                  type: string
                  format: binary
                data:
                  $ref: '#/components/schemas/CommonRequestSchemas/properties/MultipartJsonData'
              type: object
          application/json:
            schema:
              properties:
                rate:
                  $ref: '#/components/schemas/PluginReview/properties/rate'
                title:
                  $ref: '#/components/schemas/PluginReview/properties/title'
                text:
                  $ref: '#/components/schemas/PluginReview/properties/text'
                name:
                  $ref: '#/components/schemas/PluginReview/properties/name'
                job_title:
                  $ref: '#/components/schemas/PluginReview/properties/job_title'
                company:
                  $ref: '#/components/schemas/PluginReview/properties/company'
                company_url:
                  $ref: '#/components/schemas/PluginReview/properties/company_url'
                profile_url:
                  $ref: '#/components/schemas/PluginReview/properties/profile_url'
                is_active:
                  $ref: '#/components/schemas/PluginReview/properties/is_featured'
              type: object
      responses:
        '201':
          description: 'The created review.'
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/PluginReview'
        '400':
          $ref: '#/components/responses/400'
        '401':
          $ref: '#/components/responses/401'
        '402':
          $ref: '#/components/responses/402'
        '404':
          $ref: '#/components/responses/404'
    parameters:
      -
        $ref: '#/components/parameters/product_id'
      -
        $ref: '#/components/parameters/user_id'
      -
        $ref: '#/components/parameters/license_id'
  '/products/{product_id}/users/{user_id}/payments.json':
    get:
      tags:
        - Users
      summary: 'List all payments'
      description: 'Retrieve the payment collection associated with a user.'
      operationId: users/list-payments
      parameters:
        -
          $ref: '#/components/parameters/fields'
        -
          $ref: '#/components/parameters/offset'
        -
          $ref: '#/components/parameters/count'
        -
          name: extended
          in: query
          description: 'If `true`, loads linked user, plan and subscription.'
          required: false
          schema:
            type: boolean
            default: 'false'
        -
          name: include_addons
          in: query
          description: 'Returns the plugin add-ons'' payments as well.'
          schema:
            type: boolean
            default: 'false'
        -
          name: include_bundles
          in: query
          description: 'Returns the plugin bundles'' payments as well.'
          schema:
            type: boolean
            default: 'false'
        -
          name: filter
          in: query
          description: 'Filter the payments by the status.'
          schema:
            type: string
            default: all
            enum:
              - all
              - refunds
              - not_refunded
              - not_refunded_renewals
        -
          $ref: '#/components/parameters/billing_cycle'
      responses:
        '200':
          description: 'Payment collection.'
          content:
            application/json:
              schema:
                properties:
                  payments: { type: array, items: { allOf: [{ $ref: '#/components/schemas/Payment' }, { properties: { currency: { description: '3-char currency code. (Only available when `extended` is set to `true`.)', type: string, maxLength: 3, minLength: 3, enum: [usd, eur, gbp], nullable: false }, plan_name: { description: 'Name of the plan associated with the subscription. (Only available when `extended` is set to `true`.)', type: string, example: Professional, nullable: true }, email: { description: 'Email of the user associated with the subscription. (Only available when `extended` is set to `true`.)', type: string, example: foo@freemius.com, nullable: true }, url: { description: 'URL of the installation associated with the subscription. (Only available when `extended` is set to `true`.)', type: string, example: 'https://example.com', nullable: true }, billing_cycle: { description: 'The billing cycle of the subscription in number of months. 1 means monthly, 12 means annually, 0 means lifetime usually when subscriptions are created for lifetime trials. (Only available when `extended` is set to `true`.)', type: number, enum: [1, 12, 0] } }, type: object }] } }
                  discounts: { type: array, items: { $ref: '#/components/schemas/Discount' } }
                type: object
        '401':
          $ref: '#/components/responses/401'
        '402':
          $ref: '#/components/responses/402'
        '404':
          $ref: '#/components/responses/404'
    parameters:
      -
        $ref: '#/components/parameters/product_id'
      -
        $ref: '#/components/parameters/user_id'
  '/products/{product_id}/users/{user_id}/payments/{payment_id}/invoice.pdf':
    get:
      tags:
        - Users
      summary: 'Download invoice'
      description: 'Download invoice of a payment of a user. Use this endpoint to securely download the invoice of a payment belonging to a user. This is useful for implementing your own Customer Portal with download links to invoices.'
      operationId: users/download-invoice
      parameters:
        -
          $ref: '#/components/parameters/fields'
      responses:
        '200':
          description: 'PDF invoice'
          content:
            application/pdf: {  }
        '400':
          $ref: '#/components/responses/400'
        '401':
          $ref: '#/components/responses/401'
        '402':
          $ref: '#/components/responses/402'
        '404':
          $ref: '#/components/responses/404'
    parameters:
      -
        $ref: '#/components/parameters/product_id'
      -
        $ref: '#/components/parameters/user_id'
      -
        $ref: '#/components/parameters/payment_id'
  '/products/{product_id}/users/{user_id}/subscriptions.json':
    get:
      tags:
        - Users
      summary: 'List all subscriptions'
      description: 'Retrieve the subscription collection associated with a user.'
      operationId: users/list-subscriptions
      parameters:
        -
          name: extended
          in: query
          description: 'Enrich the subscriptions with the plan name, install URL & title, and user email.'
          required: false
          schema:
            type: boolean
            default: 'false'
        -
          name: filter
          in: query
          description: 'Filter the subscriptions by the status.'
          schema:
            type: string
            default: all
            enum:
              - all
              - active
              - cancelled
        -
          name: billing_cycle
          in: query
          description: 'Filter by billing cycle.'
          required: false
          schema:
            type: string
            enum:
              - 1
              - 12
        -
          $ref: '#/components/parameters/gateway'
        -
          $ref: '#/components/parameters/fields'
        -
          $ref: '#/components/parameters/offset'
        -
          $ref: '#/components/parameters/count'
        -
          name: plan_id
          in: query
          description: 'Filter the subscriptions by the plan ID.'
          schema:
            type: string
        -
          name: sort
          in: query
          description: 'Sort the subscriptions by the ID or the next payment date.'
          schema:
            type: string
            default: id
            enum:
              - id
              - next_payment
        -
          name: search
          in: query
          description: 'Search by subscription ID, external subscription ID or user email.'
          schema:
            type: string
        -
          name: enrich_with_cancellation_discounts
          in: query
          description: 'When set to `true` enrich the subscription to include any cancellation discounts applied to the subscriptions.'
          schema:
            type: boolean
            example: 'false'
      responses:
        '200':
          description: 'Subscription collection.'
          content:
            application/json:
              schema:
                properties:
                  subscriptions: { type: array, items: { allOf: [{ $ref: '#/components/schemas/Subscription' }, { properties: { plan_name: { description: 'Name of the plan associated with the subscription. (Only available when `extended` is set to `true`.)', type: string, example: Professional, nullable: true }, email: { description: 'Email of the user associated with the subscription. (Only available when `extended` is set to `true`.)', type: string, example: foo@freemius.com, nullable: true }, url: { description: 'URL of the installation associated with the subscription. (Only available when `extended` is set to `true`.)', type: string, example: 'https://example.com', nullable: true }, title: { description: 'Title of the installation associated with the subscription. (Only available when `extended` is set to `true`.)', type: string, example: 'Website title', nullable: true }, has_subscription_cancellation_discount: { description: 'Shows whether a renewal discount was already applied to the subscription.', type: boolean, example: false, nullable: true } }, type: object }] } }
                  discounts: { description: 'The key represents the ID of the subscription', additionalProperties: { schema: FSEndpointDeveloperPluginUserSubscriptions, type: array, items: { $ref: '#/components/schemas/Discount' } } }
                type: object
        '401':
          $ref: '#/components/responses/401'
        '402':
          $ref: '#/components/responses/402'
        '404':
          $ref: '#/components/responses/404'
    parameters:
      -
        $ref: '#/components/parameters/product_id'
      -
        $ref: '#/components/parameters/user_id'
  '/products/{product_id}/users/{user_id}/tokens/checkout.json':
    post:
      tags:
        - Users
      summary: 'Create a checkout token'
      description: 'Create a 1 min long token that represents the details of the user for setting the user context in a checkout session. Please read our [documentation](help-documentation-selling-with-freemius-freemius-checkout-buy-button.md#user_token_in_checkout_new) to learn how to use it.'
      operationId: users/create-checkout-token
      responses:
        '201':
          description: 'The created checkout token.'
          content:
            application/json:
              schema:
                properties:
                  token: { example: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoxLCJwcm9kdWN0X2lkIjozLCJ0b2tlbl9leHBpcmF0aW9uIjoxNTY3ODk4NzYwfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c }
                type: object
        '401':
          $ref: '#/components/responses/401'
        '402':
          $ref: '#/components/responses/402'
        '404':
          $ref: '#/components/responses/404'
    parameters:
      -
        $ref: '#/components/parameters/product_id'
      -
        $ref: '#/components/parameters/user_id'
  '/developers/{developer_id}/products/{product_id}/plans/{plan_id}.json':
    put:
      tags:
        - Plans
      summary: 'Update a plan'
      description: "\nUpdate an existing plan by ID.\n\n> Only developers can update plans."
      operationId: plans/update
      parameters:
        -
          $ref: '#/components/parameters/developer_id'
        -
          $ref: '#/components/parameters/fields'
      requestBody:
        required: true
        content:
          application/json:
            schema:
              properties:
                name:
                  $ref: '#/components/schemas/Plan/properties/name'
                title:
                  $ref: '#/components/schemas/Plan/properties/title'
                description:
                  $ref: '#/components/schemas/Plan/properties/description'
                is_free_localhost:
                  $ref: '#/components/schemas/Plan/properties/is_free_localhost'
                is_block_features:
                  $ref: '#/components/schemas/Plan/properties/is_block_features'
                is_block_features_monthly:
                  $ref: '#/components/schemas/Plan/properties/is_block_features_monthly'
                license_type:
                  $ref: '#/components/schemas/Plan/properties/license_type'
                trial_period:
                  $ref: '#/components/schemas/Plan/properties/trial_period'
                is_require_subscription:
                  $ref: '#/components/schemas/Plan/properties/is_require_subscription'
                support_forum:
                  $ref: '#/components/schemas/Plan/properties/support_forum'
                support_kb:
                  $ref: '#/components/schemas/Plan/properties/support_kb'
                support_email:
                  $ref: '#/components/schemas/Plan/properties/support_email'
                support_phone:
                  $ref: '#/components/schemas/Plan/properties/support_phone'
                is_success_manager:
                  $ref: '#/components/schemas/Plan/properties/is_success_manager'
                is_featured:
                  $ref: '#/components/schemas/Plan/properties/is_featured'
                is_hidden:
                  $ref: '#/components/schemas/Plan/properties/is_hidden'
              type: object
      responses:
        '200':
          description: 'Plan updated'
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Plan'
        '400':
          $ref: '#/components/responses/400'
        '401':
          $ref: '#/components/responses/401'
        '402':
          $ref: '#/components/responses/402'
        '404':
          $ref: '#/components/responses/404'
      security:
        -
          ApiAuthFSACookie: []
        -
          ApiAuthFSAHeader: []
      x-remove-from-doc: true
      x-internal: true
    delete:
      tags:
        - Plans
      summary: 'Delete a plan'
      description: 'Delete a specific plan by ID.'
      operationId: plans/delete
      parameters:
        -
          $ref: '#/components/parameters/developer_id'
      responses:
        '204':
          $ref: '#/components/responses/204'
        '400':
          $ref: '#/components/responses/400'
        '401':
          $ref: '#/components/responses/401'
        '402':
          $ref: '#/components/responses/402'
        '404':
          $ref: '#/components/responses/404'
      security:
        -
          ApiAuthFSACookie: []
        -
          ApiAuthFSAHeader: []
      x-remove-from-doc: true
      x-internal: true
components:
  schemas:
    ApiError:
      properties:
        path:
          description: 'The API request path.'
          type: string
          example: ':/products/product_id/users.json'
        error:
          description: 'This object contains the error details.'
          properties:
            type:
              description: 'The type of the error encountered by the server.'
              type: string
              example: UnauthorizedAccess
            message:
              description: 'The descriptive error message.'
              type: string
              example: 'Some error has occured.'
            code:
              description: 'The error code.'
              type: string
              example: unauthorized_access
            http:
              description: 'The HTTP status code returned by the server.'
              type: integer
              example: 401
            timestamp:
              description: 'Current timestamp.'
              type: string
              example: 'Thu, 11 May 2023 11:45:30 +0000'
          type: object
        request:
          description: 'This object sends back the request payload as received by the server (both from path and from body or query).'
          type: object
          example:
            beautify: true
            format: json
          additionalProperties: true
      type: object
      x-internal: true
    CommonEnums:
      description: 'Some enums that are common to many entities.'
      properties:
        ProductType:
          type: string
          enum:
            - plugin
            - theme
            - widget
            - template
        RefundPolicy:
          type: string
          enum:
            - flexible
            - moderate
            - strict
        RenewalsDiscountType:
          description: 'The type of renewals discount, percentage or dollar.'
          type: string
          enum:
            - percentage
            - dollar
        AuthenticationType:
          description: 'The type of authentication. If `app2fa` is set, the person has signed for 2FA authentication.'
          type: string
          enum:
            - app2fa
            - password
        EmailStatus:
          description: 'The status of the last email sent to the user.'
          type: string
          enum:
            - delivered
            - bounce
            - dropped
        BillingCycle:
          description: 'The billing cycle of the subscription in number of months. 1 means monthly, 12 means annually, 0 means lifetime usually when subscriptions are created for lifetime trials.'
          type: number
          enum:
            - 1
            - 12
            - 0
        PlanPeriod:
          description: 'The billing cycle or period of a plan.'
          type: string
          enum:
            - monthly
            - annual
            - lifetime
        PersonType:
          description: 'The type of the person. A developer is a person who sells software through the Freemius platform, a user is a person who buys software through the Freemius platform.'
          type: string
          enum:
            - developer
            - user
        DiscountType:
          description: 'The type of the discount. "percentage" means the discount is a percentage of the price, "dollar" means the discount is a fixed amount.'
          type: string
          enum:
            - dollar
            - percentage
        PaymentMethodType:
          description: 'The payment method selected for the purchase.'
          type: string
          default: cc
          enum:
            - cc
            - paypal
            - ideal
        Currency:
          description: '3-char currency code.'
          type: string
          maxLength: 3
          minLength: 3
          enum:
            - usd
            - eur
            - gbp
          nullable: false
        PaymentType:
          description: 'The type of the payment.'
          type: string
          default: payment
          enum:
            - payment
            - refund
            - disputed
            - won_dispute
            - lost_dispute
            - chargeback
          nullable: false
        BusinessModel:
          description: 'The product sales model.'
          type: string
          enum:
            - free
            - freemium
            - premium
          example:
            - freemium
        EventLogState:
          description: 'State of the event log. It essentially says whether the event was processed through the webhook or not.'
          type: string
          enum:
            - processed
            - pending
            - canceled
            - error
      type: object
      x-internal: true
    CommonProperties:
      description: 'This schema lists the common properties shared by various other schemas or entities.'
      properties:
        id:
          description: 'The unique identifier of the entity.'
          type: string
          format: int64
          minimum: 1
          example: '123456'
          nullable: false
        created:
          description: 'The date and time the entity was created, under UTC timezone.'
          type: string
          format: date-time
          example: '2025-01-01 00:00:00'
          nullable: false
        updated:
          description: 'The date and time the entity was updated, under UTC timezone. If `null` then the entity was never updated since its creation.'
          type: string
          format: date-time
          example: '2025-01-01 00:00:00'
          nullable: true
        icon:
          description: 'The icon of the entity, must be a valid JPG, PNG or GIF image, with dimension not exceeding 300px by 300px. Max allowed size is 200KB'
          type: string
          format: binary
        plugin_id:
          description: 'The ID of the product the entity belongs to.'
          type: string
          format: int64
          minimum: 1
          example: '123456'
          nullable: false
        plugin_id_nullable:
          description: 'The ID of the product the entity belongs to. Null means it has not been associated with a product yet.'
          type: string
          format: int64
          minimum: 1
          example: '123456'
          nullable: true
        environment:
          description: 'The environment the entity belongs to. 0 means it belongs to the production environment, 1 means it belongs to the sandbox environment.'
          type: number
          enum:
            - 1
            - 0
          example: 0
          nullable: false
        user_id:
          description: 'The ID of the user the entity belongs to.'
          type: string
          format: int64
          minimum: 1
          example: '123456'
          nullable: false
        install_id:
          description: 'The ID of the installation or site the entity is associated with.'
          type: string
          format: int64
          minimum: 1
          example: '123456'
          nullable: false
        install_id_nullable:
          description: 'The ID of the installation or site the entity is associated with, a `null` value means it has not been associated with an installation yet.'
          type: string
          format: int64
          minimum: 1
          example: '123456'
          nullable: true
        plan_id:
          description: 'The ID of the plan associated with the entity.'
          type: string
          format: int64
          minimum: 1
          example: '123456'
          nullable: false
        subscription_id:
          description: 'The ID of the subscription associated with the entity.'
          type: string
          format: int64
          minimum: 1
          example: '123456'
          nullable: false
        subscription_id_nullable:
          description: 'The ID of the subscription associated with the entity.'
          type: string
          format: int64
          minimum: 1
          example: '123456'
          nullable: true
        payment_id_nullable:
          description: 'The ID of the payment associated to the entity.'
          type: string
          format: int64
          minimum: 1
          example: '123456'
          nullable: true
        plan_id_nullable:
          description: 'The ID of the plan associated with the entity.'
          type: string
          format: int64
          minimum: 1
          example: '123456'
          nullable: true
        pricing_id:
          description: 'The ID of the pricing associated with the entity.'
          type: string
          format: int64
          minimum: 1
          example: '123456'
          nullable: false
        pricing_id_nullable:
          description: 'The ID of the pricing associated with the entity.'
          type: string
          format: int64
          minimum: 1
          example: '123456'
          nullable: true
        license_id:
          description: 'The ID of the license associated with the entity.'
          type: string
          format: int64
          minimum: 1
          example: '123456'
          nullable: false
        license_id_nullable:
          description: 'The ID of the license associated with the entity.'
          type: string
          format: int64
          minimum: 1
          example: '123456'
          nullable: true
        coupon_id:
          description: 'The ID of the coupon associated with the entity.'
          type: string
          format: int64
          minimum: 1
          example: '123456'
          nullable: false
        coupon_id_nullable:
          description: 'The ID of the coupon associated with the entity.'
          type: string
          format: int64
          minimum: 1
          example: '123456'
          nullable: true
        coupon_code:
          description: 'Coupon code associated with the cart.'
          type: string
          example: BLACKFRIDAY2024
          nullable: true
        ip_nullable:
          description: 'The IP address associated with the entity.'
          type: string
          format: ipv4|ipv6
          example: 0.0.0.0
          nullable: true
        ip:
          description: 'The IP address associated with the entity.'
          type: string
          format: ipv4|ipv6
          example: 0.0.0.0
          nullable: false
        country_code_nullable:
          description: 'The [ISO 3166-1 alpha 2](http://www.wikiwand.com/en/ISO_3166-1_alpha-2) two-letter country code associated with the entity.'
          type: string
          example: us
          nullable: true
        country_code:
          description: 'The [ISO 3166-1 alpha 2](http://www.wikiwand.com/en/ISO_3166-1_alpha-2) two-letter country code associated with the entity.'
          type: string
          example: us
          nullable: false
        zip_postal_code:
          description: 'The postal/zip code of the location.'
          type: string
          example: '92710'
          nullable: false
        zip_postal_code_nullable:
          description: 'The postal/zip code of the location.'
          type: string
          example: '92710'
          nullable: true
        vat_id_nullable:
          description: 'The business VAT number (EU or UK territories) or other tax ID (for example Sales Tax ID for the US).'
          type: string
          example: GB12345678
          nullable: true
        vat:
          description: 'The actual tax amount. It could be any kind of tax, not necessarily VAT. For example we support US Sales Tax.'
          type: number
          default: 0
          example: 1.24
          nullable: false
        uid:
          description: 'Unique identifier of the caller. The UID must be same when pinging and when activating or deactivating a license. The generation of the UID is a responsibility of the client.'
          type: string
          format: uid
          maxLength: 32
          minLength: 32
          example: 7W131pej6bJYV8WYM9KgGoBNB9bCiSrY
        user_id_nullable:
          description: 'The ID of the user the entity belongs to. If NULL then still not associated to any user.'
          type: string
          format: int64
          minimum: 1
          example: '123456'
          nullable: true
        url:
          description: 'The URL of the entity.'
          type: string
          example: 'https://www.example.com'
      type: object
      x-internal: true
    CommonRequestSchemas:
      description: 'Some request body schemas that are common to many endpoints.'
      properties:
        MultipartJsonData:
          description: 'The JSON data of the endpoint, matching the same schema as the json request body. Must be a valid JSON object.'
          type: string
          format: json
          example: '{"name":"My Product"}'
      type: object
      x-internal: true
    Migration:
      description: 'Resource explaining different relational data for migrated entities. For example if you''d want to migrate your product from EDD to Freemius, then your existing subscriptions, payments, licenses etc would have a specific value in their `source` property. To get support migrating from other platform please see our [documentation](help-documentation-migration.md).'
      properties:
        source_external_id:
          description: 'The source of the migration data. To get support migrating from other platform please see our [documentation](help-documentation-migration.md).'
          type: string
          enum:
            - freemius
            - edd
            - others
            - easydigitaldownloads
            - woo
            - wc
            - woocommerce
            - gumroad
            - cc
            - codecanyon
            - tf
            - themeforest
            - appsumo
            - sendowl
            - whmcs
            - ls
            - lemonsqueezy
          example: ls
        source:
          description: "\nThe source of the migration data. To get support migrating from other platform please see our [documentation](help-documentation-migration.md).\n\n* `0` - Freemius\n* `1` - Other\n* `2` - Easy Digital Downloads (EDD)\n* `3` - WooCommerce (WC)\n* `4` - Rating Widget\n* `5` - Gumroad\n* `6` - CodeCanyon\n* `7` - ThemeForest\n* `8` - AppSumo\n* `9` - SendOwl\n* `10` - WHMCS\n* `11` - Lemon Squeezy\n\n     "
          type: number
          enum:
            - 0
            - 1
            - 2
            - 3
            - 4
            - 5
            - 6
            - 7
            - 8
            - 9
            - 10
            - 11
      type: object
      x-internal: true
    CheckoutUpgradeLink:
      properties:
        url:
          description: 'The URL to the checkout page.'
          type: string
          format: uri
        settings:
          description: 'The settings used to generate the link. This can be fed as-is to the [Freemius Checkout JS SDK](https://github.com/Freemius/freemius-checkout-js) if you''re using modals in your website.'
          type: object
          example:
            plugin_id: 1
            plan_id: 2
            licenses: unlimited
          additionalProperties: true
        expires:
          description: 'The expiration date of the link.'
          type: string
          format: date-time
      type: object
      x-internal: true
    BankAccount:
      properties:
        id:
          $ref: '#/components/schemas/CommonProperties/properties/id'
        created:
          $ref: '#/components/schemas/CommonProperties/properties/created'
        updated:
          $ref: '#/components/schemas/CommonProperties/properties/updated'
        person_id:
          description: 'ID of the person.'
          type: number
        person_type:
          $ref: '#/components/schemas/CommonEnums/properties/PersonType'
        account_last4:
          description: 'Last 4 digits of the account number.'
          type: string
        name:
          description: 'Name of the account holder.'
          type: string
        phone:
          description: 'Phone number of the account holder.'
          type: string
        address_street:
          description: 'Address line one of the account holder.'
          type: string
        address_apt:
          description: 'Address line two of the account holder.'
          type: string
          nullable: true
        address_city:
          description: 'City of the account holder.'
          type: string
        address_state:
          description: 'State of the account holder.'
          type: string
          nullable: true
        address_zip:
          description: 'ZIP or postal code of the account holder.'
          type: string
        address_country_code:
          $ref: '#/components/schemas/CommonProperties/properties/country_code'
        bank_name:
          description: 'Name of the bank.'
          type: string
        bank_city_state:
          description: 'City and state of the bank.'
          type: string
        bank_country_code:
          $ref: '#/components/schemas/CommonProperties/properties/country_code'
        swift:
          description: 'Swift code of the bank.'
          type: string
        ifsc:
          description: 'IFSC number of Indian banks only.'
          type: string
          nullable: true
        sort_code:
          description: '6 digits Sort code of UK banks only.'
          type: string
          pattern: '^\d{6}$'
          nullable: true
        aba_rtn:
          description: '9 digits Routing number for US banks only.'
          type: string
          pattern: '^\d{9}$'
          nullable: true
        wise_account_email:
          description: 'Email account for Wise banks only.'
          type: string
          nullable: true
      type: object
      x-internal: true
    BetaParticipation:
      description: 'A Beta participation represents a choice by the user to utilize the beta version of the product.'
      properties:
        id:
          $ref: '#/components/schemas/CommonProperties/properties/id'
        created:
          $ref: '#/components/schemas/CommonProperties/properties/created'
        updated:
          $ref: '#/components/schemas/CommonProperties/properties/updated'
        user_id:
          $ref: '#/components/schemas/CommonProperties/properties/user_id'
        plugin_id:
          $ref: '#/components/schemas/CommonProperties/properties/plugin_id_nullable'
        install_id:
          $ref: '#/components/schemas/CommonProperties/properties/install_id_nullable'
        is_beta:
          description: 'Whether the product user is participating in the beta program.'
          type: boolean
      type: object
      x-internal: true
    Billing:
      description: 'Representation of billing details associated with a person or a business.'
      properties:
        id:
          $ref: '#/components/schemas/CommonProperties/properties/id'
        created:
          $ref: '#/components/schemas/CommonProperties/properties/created'
        updated:
          $ref: '#/components/schemas/CommonProperties/properties/updated'
        business_name:
          description: 'The name of the business.'
          type: string
          example: 'Freemius, Inc.'
        first:
          description: 'The first name used in the billing.'
          type: string
          example: John
        last:
          description: 'The last name used in the billing.'
          type: string
          example: Doe
        email:
          description: 'The email used in the billing.'
          type: string
          example: foo@freemius.com
        phone:
          description: 'The phone number used in the billing.'
          type: string
          example: 555-555-5555
        website:
          description: 'The website used in the billing.'
          type: string
          example: 'https://freemius.com'
        tax_id:
          description: 'The business VAT number (EU or UK territories) or other tax ID (for example Sales Tax ID for the US).'
          type: string
          example: GB123456789
        address_street:
          description: 'The street address used in the billing.'
          type: string
          example: '21st Jump Street'
        address_apt:
          description: 'The street address 2 used in the billing.'
          type: string
          example: 'Block II'
        address_city:
          description: 'The city used in the billing.'
          type: string
          example: Atlanta
        address_country:
          description: 'The country used in the billing.'
          type: string
          example: 'United States'
        address_country_code:
          $ref: '#/components/schemas/CommonProperties/properties/country_code'
        address_state:
          description: 'The state of the location.'
          type: string
          example: 'New York'
        address_zip:
          description: 'ZIP or postal code.'
          type: string
          example: '00001'
      type: object
    Cart:
      description: 'A cart represents a buyer''s intent to purchase a product. The state of the cart is based on the action performed by the buyer. You can read our [documentation](help-documentation-marketing-automation-cart-abandonment-recovery.md) to learn more about it.'
      properties:
        id:
          $ref: '#/components/schemas/CommonProperties/properties/id'
        created:
          $ref: '#/components/schemas/CommonProperties/properties/created'
        updated:
          $ref: '#/components/schemas/CommonProperties/properties/updated'
        status:
          description: 'The status of the cart.'
          type: string
          default: visit
          enum:
            - pricing_visit
            - visit
            - abandoned
            - completed
            - email_1_sent
            - email_2_sent
            - email_3_sent
            - recovered
        mode:
          description: "The mode the checkout app was opened in, when the cart was created. For example\n\n- `dashboard`: The checkout was opened through our [WordPress SDK](help-documentation-wordpress-sdk.md).\n- `dialog`: The checkout was opened through our [JavaScript SDK](help-documentation-selling-with-freemius-freemius-checkout-buy-button.md).\n- `page`: The checkout was opened directly."
          type: string
          default: dialog
          enum:
            - dashboard
            - dialog
            - page
        payment_method:
          $ref: '#/components/schemas/CommonEnums/properties/PaymentMethodType'
        plugin_id:
          $ref: '#/components/schemas/CommonProperties/properties/plugin_id'
        plan_id:
          $ref: '#/components/schemas/CommonProperties/properties/plan_id_nullable'
        pricing_id:
          $ref: '#/components/schemas/CommonProperties/properties/pricing_id_nullable'
        is_trial:
          description: 'Whether the plan is a trial.'
          type: boolean
        billing_cycle:
          $ref: '#/components/schemas/CommonEnums/properties/BillingCycle'
        install_id:
          $ref: '#/components/schemas/CommonProperties/properties/install_id_nullable'
        coupon_id:
          $ref: '#/components/schemas/CommonProperties/properties/coupon_id_nullable'
        country_code:
          $ref: '#/components/schemas/CommonProperties/properties/country_code_nullable'
        zip_postal_code:
          $ref: '#/components/schemas/CommonProperties/properties/zip_postal_code'
        vat_id:
          $ref: '#/components/schemas/CommonProperties/properties/vat_id_nullable'
        user_id:
          $ref: '#/components/schemas/CommonProperties/properties/user_id_nullable'
        email:
          description: 'The prospect''s email address.'
          type: string
          example: doe@example.com
        first:
          description: 'The prospect''s first name.'
          type: string
          example: John
        last:
          description: 'The prospect''s last name.'
          type: string
          example: Doe
        ip:
          $ref: '#/components/schemas/CommonProperties/properties/ip'
        url:
          description: 'The page URL containing the checkout.'
          type: string
          example: 'https://example.com/pricing'
        environment:
          $ref: '#/components/schemas/CommonProperties/properties/environment'
        is_disabled:
          description: 'Cart supports [recovery campaign](help-documentation-marketing-automation-cart-abandonment-recovery.md). If disabled, the recovery campaign will be stopped.'
          type: boolean
          default: 'false'
        is_unsubscribed:
          description: 'If set to `true`, the cart recovery campaign will be non-functional and cannot be re-enabled. This happens if the prospect has clicked the "unsubscribe" link from any of the cart recovery emails.'
          type: boolean
          default: 'false'
        visited:
          description: 'The first time the prospect visited the checkout when the cart was being created.'
          type: string
          format: date-time
          example: '2025-01-01 00:00:00'
          nullable: true
        completed:
          description: 'The cart completion date.'
          type: string
          format: date-time
          example: '2025-01-01 00:00:00'
          nullable: true
        price:
          description: 'The cart''s original price.'
          type: number
          format: float
          example: '19.99'
      type: object
    Coupon:
      description: 'A coupon can be used during the checkout to apply some discounts.'
      properties:
        id:
          $ref: '#/components/schemas/CommonProperties/properties/id'
        created:
          $ref: '#/components/schemas/CommonProperties/properties/created'
        updated:
          $ref: '#/components/schemas/CommonProperties/properties/updated'
        entity_id:
          description: 'The ID of the entity the coupon belongs to.'
          type: string
          format: int64
          minimum: 1
          example: 12345
          nullable: false
        entity_type:
          description: 'The type of the entity the coupon belongs to.'
          type: string
          enum:
            - plugin
            - store
            - marketplace
          example: plugin
        plans:
          description: 'Comma separated IDs of plans the coupon would work for. If `null`, coupon supports all plans.'
          type: string
          example: '123,654,8757'
          nullable: true
        licenses:
          description: 'Comma separated licenses quota limits. If `null`, coupon supports all license limits. `0` is used for an unlimited-site license.'
          type: string
          example: '1,5,10,0'
          nullable: true
        billing_cycles:
          description: 'Comma separated billing cycles. If `null`, coupon supports all billing cycles. `0` is used for lifetime billing cycle.'
          type: string
          example: '1,12'
          nullable: true
        code:
          description: 'The coupon code.'
          type: string
          example: BLACKFRIDAY2024
        discount:
          description: 'The discount amount.'
          type: integer
        discount_type:
          $ref: '#/components/schemas/CommonEnums/properties/DiscountType'
        start_date:
          description: 'Date and time from when the coupon will be activated.'
          type: string
          format: date-time
          example: '2025-04-01 11:13:28'
        end_date:
          description: 'Date and time, after which the coupon will be expired.'
          type: string
          format: date-time
          example: '2025-04-30 19:17:21'
        redemptions:
          description: 'The total number of redemptions of this coupon.'
          type: integer
        redemptions_limit:
          description: 'The total number of redemptions limit of this coupon.'
          type: integer
          nullable: true
        has_renewals_discount:
          description: 'Whether the coupon also supports discount for renewals or first payment only.'
          type: boolean
        has_addons_discount:
          description: 'Whether the coupon supports discount for add-ons or not.'
          type: boolean
        is_one_per_user:
          description: 'Whether to limit the coupon usage one per user.'
          type: boolean
        is_active:
          description: 'Whether the coupon is active. Use this flag to temporarily disable the coupon.'
          type: boolean
        user_type:
          description: 'The user type the coupon is applicable to.'
          type: string
          default: all
          enum:
            - all
            - new
            - current
            - previous
            - customer
            - migrated
        source:
          $ref: '#/components/schemas/Migration/properties/source'
      type: object
    CouponEntity:
      description: 'Represents a link between coupons to various special entities. Example: Affiliate coupon tracking, cart abandonment recovery of a product.'
      properties:
        id:
          $ref: '#/components/schemas/CommonProperties/properties/id'
        created:
          $ref: '#/components/schemas/CommonProperties/properties/created'
        updated:
          $ref: '#/components/schemas/CommonProperties/properties/updated'
        coupon_id:
          description: 'The ID of the coupon.'
          type: number
          example: 12345
        entity_id:
          description: 'The ID of the entity.'
          type: string
          format: int64
          minimum: 1
          example: 12345
          nullable: false
        entity_type:
          description: 'The type of the entity (Usually `2` which means it is a product or `20` which means it is an affiliate).'
          type: integer
          example: 2
        type:
          description: 'The special coupon type.'
          type: string
          enum:
            - affiliate
            - renewals_discount
            - manual_renewals_discount
            - subscription_cancellation
            - cart_recovery
            - exit_intent
      type: object
    CouponEntityEnriched:
      description: 'A coupon associated with a special checkout cart on conversions and renewals to reduce churn rate.'
      type: object
      allOf:
        -
          $ref: '#/components/schemas/CouponEntity'
        -
          properties:
            code:
              $ref: '#/components/schemas/Coupon/properties/code'
            redemptions:
              $ref: '#/components/schemas/Coupon/properties/redemptions'
            discount:
              $ref: '#/components/schemas/Coupon/properties/discount'
            discount_type:
              $ref: '#/components/schemas/Coupon/properties/discount_type'
            discounts:
              description: 'The discount amount for each currency'
              type: object
              example:
                usd: 10
                eur: 9
                gbp: 8
              additionalProperties:
                type: number
                format: int
            has_renewals_discount:
              $ref: '#/components/schemas/Coupon/properties/has_renewals_discount'
          type: object
      x-internal: true
    Customer:
      description: "Class Customer\n\nAn entity to store the connection between a user to its gateway's customer ID."
      properties:
        id:
          $ref: '#/components/schemas/CommonProperties/properties/id'
        created:
          $ref: '#/components/schemas/CommonProperties/properties/created'
        updated:
          $ref: '#/components/schemas/CommonProperties/properties/updated'
        user_id:
          $ref: '#/components/schemas/CommonProperties/properties/user_id'
        external_id:
          description: 'The external ID from the gateway.'
          type: string
        gateway:
          description: 'The gateway used for the purchase.'
          type: string
          enum:
            - paypal
            - stripe
            - stripe_eu
            - test
      type: object
      x-internal: true
    Developer:
      description: 'A developer is someone who has registered to sell products on the Freemius platform.'
      properties:
        email:
          description: 'Email address of the person.'
          type: string
          example: jane@example.com
        first:
          description: 'First name of the person.'
          type: string
          example: Jane
        last:
          description: 'Last name of the person.'
          type: string
          example: Doe
        picture:
          description: 'Profile picture URL.'
          type: string
          example: 'https://example.com/profile-pic.jpg'
        ip:
          description: 'The IP address (v4 or v6).'
          type: string
          format: ipv4|ipv6
          example: 127.0.0.1
          nullable: true
        is_verified:
          description: 'Whether the person is trusted or not.'
          type: boolean
          example: 'true'
        auth:
          $ref: '#/components/schemas/CommonEnums/properties/AuthenticationType'
        secret_key:
          description: 'The secret key associated with the entity for authorization.'
          type: string
          example: sk_a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6
        public_key:
          description: 'The public key associated with the entity for authorization.'
          type: string
          example: pk_a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6
        id:
          $ref: '#/components/schemas/CommonProperties/properties/id'
        created:
          $ref: '#/components/schemas/CommonProperties/properties/created'
        updated:
          $ref: '#/components/schemas/CommonProperties/properties/updated'
        paypal_email:
          description: 'The legacy PayPal email of the developer. Please use the new billing instead.'
          type: string
          example: payout@example.com
          deprecated: true
        security_email:
          description: 'Additional address of the developer where Freemius will send security related emails.'
          type: string
          example: security@example.com
        is_trusted:
          type: boolean
        earnings:
          description: 'Developer''s paid out gross revenue (excluding chargeback fees, payout fees, and refund fees).'
          type: number
          format: float
          example: '1000.00'
        last_cycle_earnings:
          description: 'Developer''s unpaid gross revenue. Necessary for properly calculating the commission.'
          type: number
          format: float
          example: '100.00'
        commission:
          description: "Commission structure. The structure `{1000: 0.3, 5000: 0.2, above: 0.1}`, means\nthat there's 30% commission on up to $1,000 rev, 20% on the revenues from $1,001-$5,000 and 10% after $5,001."
          type: string
          format: json
          example: '{"above":0.1}'
      type: object
    Discount:
      description: 'Discount entity holding the relation between a gateway entity and a coupon.'
      properties:
        id:
          $ref: '#/components/schemas/CommonProperties/properties/id'
        created:
          $ref: '#/components/schemas/CommonProperties/properties/created'
        updated:
          $ref: '#/components/schemas/CommonProperties/properties/updated'
        entity_id:
          description: 'The ID of the related entity.'
          type: string
          format: int64
          minimum: 1
        entity_type:
          description: 'The type of the related entity. Defaults to `payment`.'
          type: string
          default: payment
          enum:
            - payment
            - subscription
        type:
          description: 'The type of discount. Possible values are `prorate` and `subscription_cancellation`. Defaults to `prorate`.'
          type: string
          default: prorate
          enum:
            - prorate
            - subscription_cancellation
        discount:
          description: 'Discount amount in USD.'
          type: number
          format: float
          example: '10.0'
        coupon_id:
          description: 'The ID of the related coupon.'
          type: string
          format: int64
          minimum: 1
      type: object
    EmailTemplate:
      description: 'Represents an email template. This feature is not fully made and should not be used.'
      properties:
        id:
          $ref: '#/components/schemas/CommonProperties/properties/id'
        created:
          $ref: '#/components/schemas/CommonProperties/properties/created'
        updated:
          $ref: '#/components/schemas/CommonProperties/properties/updated'
        plugin_id:
          $ref: '#/components/schemas/CommonProperties/properties/plugin_id'
        category:
          description: 'The category of the email template.'
          type: string
          example: user_register
        subject:
          description: 'The subject of the email.'
          type: string
          example: 'Welcome to Freemius!'
        plain:
          description: 'The plaintext version of the email.'
          type: string
        html:
          description: 'The HTML version of the email.'
          type: string
      type: object
      x-internal: true
    EventLog:
      description: 'A record of an event logged in the system.'
      properties:
        state:
          $ref: '#/components/schemas/CommonEnums/properties/EventLogState'
        id:
          $ref: '#/components/schemas/CommonProperties/properties/id'
        created:
          $ref: '#/components/schemas/CommonProperties/properties/created'
        updated:
          $ref: '#/components/schemas/CommonProperties/properties/updated'
        type:
          description: 'The type of event. See our documented list of the available [event types](help-documentation-marketing-automation-events-webhooks.md#event_types).'
          type: string
          example: license.activated
        developer_id:
          description: 'The ID of the developer.'
          type: string
          format: int64
          minimum: 1
          example: '1234'
        plugin_id:
          $ref: '#/components/schemas/CommonProperties/properties/plugin_id_nullable'
        user_id:
          $ref: '#/components/schemas/CommonProperties/properties/user_id_nullable'
        install_id:
          $ref: '#/components/schemas/CommonProperties/properties/install_id_nullable'
        data:
          description: 'The details of the triggered event. This can be a `string` showing ID of the associated entity, an `object` with additional information of the event, or array of objects.'
          nullable: true
        event_trigger:
          description: 'The type of trigger for the event.'
          type: string
          enum:
            - system
            - developer
            - plugin
            - user
            - install
          example: system
        process_time:
          description: 'The time the event was processed. If it is `null`, the event is pending.'
          type: string
          format: date-time
          example: '2025-01-01 12:00:00'
          nullable: true
      type: object
    Feature:
      description: 'A feature is a distinct functionality or capability of a product that delivers value to users by addressing specific needs or solving problems.'
      properties:
        id:
          $ref: '#/components/schemas/CommonProperties/properties/id'
        created:
          $ref: '#/components/schemas/CommonProperties/properties/created'
        updated:
          $ref: '#/components/schemas/CommonProperties/properties/updated'
        plugin_id:
          description: 'The ID of the Plugin.'
          type: string
          format: int64
          minimum: 1
          example: '1234'
        title:
          description: 'The title of the feature.'
          type: string
          example: 'Pageviews per month'
        description:
          description: 'The description of the feature, up to 256 characters. This will be displayed as the description in the tooltip on the pricing page.'
          type: string
          example: 'The number of times a page is loaded.'
        is_featured:
          description: 'Whether the feature is highlighted and will be shown in the main pricing table. If set as `false`, the feature will be only shown in the plans'' comparison table.'
          type: boolean
          example: 'true'
      type: object
    FeatureEnriched:
      type: object
      allOf:
        -
          $ref: '#/components/schemas/Feature'
        -
          properties:
            value:
              description: 'The value of the feature associated with the plan. For example the feature name could be "AI Credits" and the value could be "1000".'
              type: string
              example: '1000 Units'
            plan_id:
              $ref: '#/components/schemas/CommonProperties/properties/plan_id'
          type: object
    FeaturePlan:
      properties:
        id:
          $ref: '#/components/schemas/CommonProperties/properties/id'
        created:
          $ref: '#/components/schemas/CommonProperties/properties/created'
        updated:
          $ref: '#/components/schemas/CommonProperties/properties/updated'
        plan_id:
          description: 'The ID of the plan that the feature is associated.'
          type: string
          format: int64
          minimum: 1
          example: '1234'
        value:
          description: 'The value associated with the feature.'
          type: string
          example: 25k
          nullable: true
      type: object
      x-internal: true
    Install:
      description: 'Represents an installation of a product on a site. For WordPress products (themes, plugins) it can or cannot have a license. For SaaS or downloadable software, it would always have a license. Please see license activation for more information.'
      properties:
        secret_key:
          description: 'The secret key associated with the entity for authorization.'
          type: string
          example: sk_a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6
        public_key:
          description: 'The public key associated with the entity for authorization.'
          type: string
          example: pk_a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6
        id:
          $ref: '#/components/schemas/CommonProperties/properties/id'
        created:
          $ref: '#/components/schemas/CommonProperties/properties/created'
        updated:
          $ref: '#/components/schemas/CommonProperties/properties/updated'
        site_id:
          description: 'The ID of the site.'
          type: string
          format: int64
          example: 1234
        plugin_id:
          $ref: '#/components/schemas/CommonProperties/properties/plugin_id'
        user_id:
          $ref: '#/components/schemas/CommonProperties/properties/user_id'
        url:
          description: 'The site URL.'
          type: string
          example: 'https://example.com'
          nullable: true
        title:
          description: 'The site title.'
          type: string
          example: 'Catwalk Designs'
          nullable: true
        version:
          description: 'The Product version.'
          type: string
          example: 1.0.0
        plan_id:
          description: 'The ID of the plan associated with the product that the install has a license activation. If `null` it means the install is using the free plan.'
          type: string
          format: int64
          minimum: 1
          example: '1234'
        license_id:
          $ref: '#/components/schemas/CommonProperties/properties/license_id_nullable'
        trial_plan_id:
          description: 'The ID of the trial license associated to the product. If this is not a trial, this will be `null`.'
          type: string
          format: int64
          minimum: 1
          example: '1234'
        trial_ends:
          description: 'The product trial license expiry date. If this is not a trial, this will be null.'
          type: string
          format: date-time
          example: '2025-01-01 00:00:00'
          nullable: true
        subscription_id:
          $ref: '#/components/schemas/CommonProperties/properties/subscription_id_nullable'
        gross:
          description: 'The gross amount the install has spent on the product. This includes one time purchase, or subscriptions and renewals.'
          type: number
          format: float
          example: 100
        country_code:
          $ref: '#/components/schemas/CommonProperties/properties/country_code_nullable'
        language:
          description: 'The language specified for the product install.'
          type: string
          example: en-GB
          nullable: true
        platform_version:
          description: 'The platform version (e.g WordPress version).'
          type: string
          example: 1.0.0
          nullable: true
        sdk_version:
          description: 'The Freemius SDK version. Only relevant for WordPress products using the Freemius [WP SDK](help-documentation-wordpress-sdk.md).'
          type: string
          example: 1.2.2
          nullable: true
        programming_language_version:
          description: 'The programming language version (e.g PHP version).'
          type: string
          example: '5.6'
          nullable: true
        is_active:
          description: 'If the product is actively installed on the site.'
          type: boolean
        is_disconnected:
          description: 'If the product is disconnected on the site.'
          type: boolean
        is_premium:
          description: 'If the install using the premium code. Relevant only for WP Products.'
          type: boolean
        is_uninstalled:
          description: 'If the product is uninstalled on the site.'
          type: boolean
        is_locked:
          description: 'If the product is locked on the site.'
          type: boolean
        source:
          $ref: '#/components/schemas/Migration/properties/source'
        upgraded:
          description: 'Time when the product was upgraded to the current version. If never upgraded since the initial installation, this will be `null`.'
          type: string
          format: date-time
          example: '2025-01-01 00:00:00'
          nullable: true
        last_seen_at:
          description: 'The last time the product was used on the site.'
          type: string
          format: date-time
          example: '2025-01-01 00:00:00'
          nullable: true
        last_served_update_version:
          description: 'The last product version update used on the site. If not updated, this will be null.'
          type: string
          example: 1.2.2
          nullable: true
      type: object
    InstallClone:
      description: 'Represents the relation between an install and its clone. These entities are usually created when a user clones the site in staging or locally.'
      properties:
        id:
          $ref: '#/components/schemas/CommonProperties/properties/id'
        created:
          $ref: '#/components/schemas/CommonProperties/properties/created'
        updated:
          $ref: '#/components/schemas/CommonProperties/properties/updated'
        install_id:
          $ref: '#/components/schemas/CommonProperties/properties/install_id'
        new_install_id:
          description: 'The ID of the newly created cloned `Install`.'
          type: string
          format: int64
          minimum: 1
          example: '1234'
          nullable: true
        install_url:
          description: 'The install''s URL (install.url) when the clone was identified.'
          type: string
          example: 'https://example.com'
        site_url:
          description: 'The URL of the site where the clone was identified.'
          type: string
          example: 'https://staging.example.com'
        state:
          description: 'The state of the clone.'
          type: string
          enum:
            - pending
            - resolved
        resolution:
          description: 'The resolution or purpose of the clone site.'
          type: string
          enum:
            - temporary_duplicate
            - new_home
            - long_term_duplicate
          nullable: true
      type: object
    InstallMetadata:
      properties:
        permissions:
          properties:
            site:
              description: 'Whether the site level tracking is on, for example the site title, URL, language etc.'
              type: boolean
            user:
              description: 'Whether the user level tracking is on, for example the user email, first and last name, etc.'
              type: boolean
            extensions:
              description: 'Whether the extensions tracking is on (for example list of plugins and themes installed on the same WordPress website).'
              type: boolean
          type: object
        id:
          $ref: '#/components/schemas/CommonProperties/properties/id'
        created:
          $ref: '#/components/schemas/CommonProperties/properties/created'
        updated:
          $ref: '#/components/schemas/CommonProperties/properties/updated'
        install_id:
          $ref: '#/components/schemas/CommonProperties/properties/install_id'
      type: object
      x-internal: true
    License:
      description: 'A license represents authorization to use available features of the product.'
      properties:
        id:
          $ref: '#/components/schemas/CommonProperties/properties/id'
        created:
          $ref: '#/components/schemas/CommonProperties/properties/created'
        updated:
          $ref: '#/components/schemas/CommonProperties/properties/updated'
        plugin_id:
          $ref: '#/components/schemas/CommonProperties/properties/plugin_id'
        user_id:
          $ref: '#/components/schemas/CommonProperties/properties/user_id_nullable'
        plan_id:
          $ref: '#/components/schemas/CommonProperties/properties/plan_id'
        pricing_id:
          $ref: '#/components/schemas/CommonProperties/properties/pricing_id_nullable'
        quota:
          description: 'The maximum number of license activations. If `null` then the license will support unlimited activations.'
          type: integer
          example: 10
          nullable: true
        activated:
          description: 'The total number of production activation the license has. This does not count local or staging environment activations.'
          type: integer
          example: 1
        activated_local:
          description: 'The number of times the license is activated on local or staging environments.'
          type: integer
          example: 1
          nullable: true
        expiration:
          description: 'The expiration date of the license. If `null` then it''s a lifetime license.'
          type: string
          format: date-time
          example: '2025-12-31 23:59:59'
          nullable: true
        secret_key:
          description: 'The license key. This is used for activating the license on the user''s site.'
          type: string
          example: sk_123FGqM456Pa786WtOp%^+67Y+;sXXz
        is_free_localhost:
          description: 'Whether the license offers unlimited local or staging environment activations.'
          type: boolean
          default: true
        is_block_features:
          description: 'Whether to block features after expiration of the license. If set to `false`, this would not block features, would only block updates.'
          type: boolean
          default: true
        is_cancelled:
          description: 'If the license is canceled from the Developer Dashboard.'
          type: boolean
        is_whitelabeled:
          description: 'Guide the [Freemius WP SDK](https://github.com/Freemius/wordpress-sdk) when the product should be running in a [white-label](help-documentation-users-account-management-license-security.md#white_label_mode) mode.'
          type: boolean
        environment:
          $ref: '#/components/schemas/CommonProperties/properties/environment'
        source:
          $ref: '#/components/schemas/Migration/properties/source'
      type: object
    LicenseEnriched:
      description: 'A license associated with a subscription or a bundle.'
      type: object
      allOf:
        -
          $ref: '#/components/schemas/License'
        -
          properties:
            parent_plan_id:
              description: 'The ID of the associated bundle license (**Only** available when `enriched` option is set).'
              type: number
            trial_ends:
              description: 'The end date of a trial subscription (**Only** available when `enriched` option is set).'
              type: string
              format: date-time
              example: '2021-01-01 00:00:00'
            subscription_id:
              description: 'The ID of the associated subscription (**Only** available when `enriched` option is set).'
              type: string
              format: int64
              minimum: 1
              example: '1234'
            subscription_total_gross:
              description: 'The total gross price associated with the subscription (**Only** available when `enriched` option is set).'
              type: number
              format: float
              example: '102.34'
            subscription_initial_amount:
              description: 'The initial amount associated with the subscription (**Only** available when `enriched` option is set).'
              type: number
              format: float
              example: '105.99'
            subscription_gateway:
              description: 'The payment gateway associated with the subscription (**Only** available when `enriched` option is set).'
              type: string
              enum:
                - paypal
                - stripe
                - test
              example: stripe
            subscription_failed_payments:
              description: 'The number of failed payments associated with the subscription (**Only** available when `enriched` option is set).'
              type: integer
              example: 2
            next_payment:
              description: 'The renewal date of the subscription (**Only** available when `enriched` option is set).'
              type: string
              format: date-time
              example: '2025-01-01 00:00:00'
              nullable: true
            parent_license_id:
              description: 'The ID of the associated bundle license. This will be populated only when the license is associated with a parent license from a bundle (**Only** available when `enriched` option is set).'
              type: string
              format: int64
              minimum: 0
              example: '1234'
            parent_license_bundle_id:
              description: 'The ID of the bundle that is associated with the parent license (**Only** available when `enriched` option is set).'
              type: string
              format: int64
              minimum: 0
              example: '1234'
            parent_plan_title:
              description: 'The title of the plan associated with the bundle (**Only** available when `enriched` option is set).'
              type: string
              example: Agency
              nullable: true
            parent_plan_name:
              description: 'The slug of the plan associated with the bundle (**Only** available when `enriched` option is set).'
              type: string
              example: agency
              nullable: true
          type: object
      x-internal: true
    MarketItem:
      description: 'Represents a product from the market, not necessarily powered by Freemius. For WordPress product this usually represents a themes or plugins installed in the same site as the Freemius powered product. Only after the user chooses to opt-in, such data is collected and sent to Freemius.'
      properties:
        id:
          $ref: '#/components/schemas/CommonProperties/properties/id'
        created:
          $ref: '#/components/schemas/CommonProperties/properties/created'
        updated:
          $ref: '#/components/schemas/CommonProperties/properties/updated'
        plugin_id:
          $ref: '#/components/schemas/CommonProperties/properties/plugin_id_nullable'
        slug:
          description: 'Product slug name.'
          type: string
          example: catwalk-reviews
        title:
          description: 'Products name.'
          type: string
          example: 'Catwalk Reviews'
        model:
          description: 'The business model of the product. We can only detect the model if the product is also integrated with Freemius.'
          type: string
          default: free
          enum:
            - free
            - premium
            - freemium
        type:
          description: 'The type of the product. Right now we only support WordPress products, i.e, plugins and themes.'
          type: string
          default: plugin
          enum:
            - plugin
            - theme
        downloads:
          description: "The number of product downloads.\n\n> We are not updating this field yet. We plan to do it in the future."
          type: integer
          example: 1000
        installs_count:
          description: "The number of product installs.\n\n> We are not updating this field yet. We plan to do it in the future."
          type: integer
          example: 1000
        last_release:
          description: "The date of the last product release/update.\n\n> We are not updating this field yet. We plan to do it in the future."
          type: string
          format: date-time
          example: '2025-01-01 00:00:00'
        newest_version:
          description: 'The version number of the latest release/update.'
          type: string
          example: 1.0.0
      type: object
    Member:
      type: object
      allOf:
        -
          $ref: '#/components/schemas/Developer'
        -
          properties:
            plugin_id:
              $ref: '#/components/schemas/CommonProperties/properties/plugin_id'
            role:
              description: 'The user role assigned to the team member.'
              type: string
              enum:
                - admin
                - developer
                - support
                - accountant
          type: object
      x-internal: true
    Note:
      description: 'A written remark that provides additional context, clarification, or explanation related to a specific record.'
      properties:
        id:
          $ref: '#/components/schemas/CommonProperties/properties/id'
        created:
          $ref: '#/components/schemas/CommonProperties/properties/created'
        updated:
          $ref: '#/components/schemas/CommonProperties/properties/updated'
        scope_entity_id:
          description: 'The ID of the scope entity that this note is associated with.'
          type: integer
          example: 12345
        scope_entity_type:
          description: 'The type of the scope entity that this note is associated with.'
          type: string
          enum:
            - plugin
            - store
        entity_id:
          description: 'The ID of the entity that this note is associated with.'
          type: integer
          example: 12345
        entity_type:
          description: 'The type of the entity that this note is associated with.'
          type: string
          enum:
            - coupon
            - user
            - payment
            - subscription
            - license
        note:
          description: 'The note.'
          type: string
          example: 'This is a note'
      type: object
      x-internal: true
    Payment:
      description: "An acknowledgement of a payment recevied for the following cases:\r\n- Initial payment of a subscription.\r\n- Renewal payment of a subscription.\r\n- One-time payment for a product.\r\n\r\nAlong with refunds, disputes, chargebacks etc."
      properties:
        user_id:
          $ref: '#/components/schemas/CommonProperties/properties/user_id'
        install_id:
          $ref: '#/components/schemas/CommonProperties/properties/install_id_nullable'
        plan_id:
          $ref: '#/components/schemas/CommonProperties/properties/plan_id'
        pricing_id:
          $ref: '#/components/schemas/CommonProperties/properties/pricing_id'
        license_id:
          $ref: '#/components/schemas/CommonProperties/properties/license_id'
        ip:
          $ref: '#/components/schemas/CommonProperties/properties/ip_nullable'
        country_code:
          $ref: '#/components/schemas/CommonProperties/properties/country_code'
        zip_postal_code:
          $ref: '#/components/schemas/CommonProperties/properties/zip_postal_code_nullable'
        vat_id:
          $ref: '#/components/schemas/CommonProperties/properties/vat_id_nullable'
        coupon_id:
          $ref: '#/components/schemas/CommonProperties/properties/coupon_id_nullable'
        user_card_id:
          description: 'The ID of the user card that was used for this payment.'
          type: string
          format: int64
          example: '12345'
        source:
          $ref: '#/components/schemas/Migration/properties/source'
        plugin_id:
          $ref: '#/components/schemas/CommonProperties/properties/plugin_id'
        external_id:
          description: 'The external ID of the gateway entity.'
          type: string
          example: abcde12345
        gateway:
          description: 'The gateway used for the purchase. The gateway will be set to `null` when purchasing a product with a 100% discount.'
          type: string
          nullable: true
        environment:
          $ref: '#/components/schemas/CommonProperties/properties/environment'
        id:
          $ref: '#/components/schemas/CommonProperties/properties/id'
        created:
          $ref: '#/components/schemas/CommonProperties/properties/created'
        updated:
          $ref: '#/components/schemas/CommonProperties/properties/updated'
        currency:
          $ref: '#/components/schemas/CommonEnums/properties/Currency'
        refund_reason:
          type: string
          example: 'Refunded due to a bug in the plugin.'
          nullable: true
        subscription_id:
          $ref: '#/components/schemas/CommonProperties/properties/subscription_id_nullable'
        payment_presentment_id:
          description: 'The ID of the presentment payment.'
          type: string
          format: int64
          minimum: 1
          example: '123456'
        gross:
          description: 'The payment amount (not including taxes).'
          type: number
          format: float
          example: 2075.45
        bound_payment_id:
          description: 'The ID of the payment that this payment is bound to, in case of a refund or chargeback/dispute.'
          type: string
          format: int64
          minimum: 1
          example: '123456'
        gateway_fee:
          description: 'The fee that the gateway took for processing this payment.'
          type: number
          format: float
          default: 0
          example: 2.99
        vat:
          $ref: '#/components/schemas/CommonProperties/properties/vat'
        is_renewal:
          description: 'If the payment is a renewal.'
          type: boolean
          default: false
        type:
          $ref: '#/components/schemas/CommonEnums/properties/PaymentType'
      type: object
    PaymentPresentment:
      description: 'Presentment part of the Payment, with gross and vat in the FX currency, along with exchange rate and conversion fee.'
      properties:
        id:
          $ref: '#/components/schemas/CommonProperties/properties/id'
        created:
          $ref: '#/components/schemas/CommonProperties/properties/created'
        updated:
          $ref: '#/components/schemas/CommonProperties/properties/updated'
        currency:
          $ref: '#/components/schemas/CommonEnums/properties/Currency'
        gross:
          description: 'The payment amount (not including taxes, in FX currency).'
          type: number
          format: float
          example: 2075.45
        vat:
          $ref: '#/components/schemas/CommonProperties/properties/vat'
        conversion_fee:
          description: 'The fee that the gateway took for conversion of FX currency (in USD).'
          type: number
          format: float
          example: 2.99
        exchange_rate:
          description: 'The gateway exchange rate to convert the currency.'
          type: number
          format: float
          example: 0.123456
      type: object
    Plan:
      description: 'A plan defines the features available to the users. It can have different set of pricing per billing cycle, quota, currency etc.'
      properties:
        id:
          $ref: '#/components/schemas/CommonProperties/properties/id'
        created:
          $ref: '#/components/schemas/CommonProperties/properties/created'
        updated:
          $ref: '#/components/schemas/CommonProperties/properties/updated'
        plugin_id:
          $ref: '#/components/schemas/CommonProperties/properties/plugin_id'
        name:
          description: 'The name of the plan. Only lowercase characters allowed.'
          type: string
          format: slug
          example: professional
        title:
          description: 'The title of the plan. This is the human readable name of the plan. Please do not add the suffix `Plan` to the title, as Freemius does that for you at various places.'
          type: string
          example: Professional
        description:
          description: 'The description of the plan.'
          type: string
          example: 'For small to medium businesses.'
          nullable: true
        is_free_localhost:
          description: 'Whether the plan offers unlimited local or staging activations with the same license.'
          type: boolean
          default: true
        is_block_features:
          description: 'Whether to block features on expiration of **annual** licenses. If `false`, does not block features but only block updates and support.'
          type: boolean
          default: true
        is_block_features_monthly:
          description: 'Whether to block particular features on expiration of **monthly** licenses. If `false`, does not block features but only block updates and support.'
          type: boolean
          default: true
        license_type:
          description: 'The type of the license. `0` for per domain license. `1` for per subdomain license.'
          type: integer
          default: 0
          enum:
            - 0
            - 1
        trial_period:
          description: 'The number of days a trial period will last. If `null` the plan does not support trials.'
          type: integer
          minimum: 1
          example: '14'
          nullable: true
        is_require_subscription:
          description: 'Whether to require a subscription payment for the trial period.'
          type: boolean
        support_kb:
          description: 'The Knowledge Base URL.'
          type: string
          example: 'https://example.com/help/documentation'
          nullable: true
        support_forum:
          description: 'The support Forum URL.'
          type: string
          example: 'https://example.com/support'
          nullable: true
        support_email:
          description: 'The support email address.'
          type: string
          example: support@example.com
          nullable: true
        support_phone:
          description: 'The support phone contact.'
          type: string
          example: 555-555-5555
          nullable: true
        is_success_manager:
          description: 'Is a personal success manager allocated with the plan.'
          type: boolean
        is_featured:
          description: 'Whether this is a featured plan.'
          type: boolean
        is_hidden:
          description: 'Whether to hide the plan from the auto-generated pricing page. Mostly relevant for WordPress products and our WordPress SDK. Please see our [pricing-page](https://github.com/Freemius/pricing-page/) library to implement your own.'
          type: boolean
      type: object
    Plugin:
      title: Product
      description: 'A **product** is a software that is being sold on Freemius. It can be a WordPress plugin, theme, SaaS, or any other software that is being sold on Freemius.'
      properties:
        selling_unit_label:
          description: 'The selling unit label of the product. For example, ''site'', ''user'', ''language'', ''credit'', etc. This is used in the pricing page and in the license key information to indicate the unit of the license key. If not set, it defaults to ''site'' for plugins and themes, ''unit'' for SaaS products, and ''activation'' for Apps.'
          type: string
          example: site
        enable_after_purchase_email_login_link:
          description: 'Indicates whether the customer portal login link is included in the after-purchase emails.'
          type: boolean
          example: true
        restrict_single_subscription_per_user:
          description: 'Indicates whether Freemius will enforce single active susbcription per user. This is available for SaaS products only.'
          type: boolean
          example: false
        secret_key:
          description: 'The secret key associated with the entity for authorization.'
          type: string
          example: sk_a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6
        public_key:
          description: 'The public key associated with the entity for authorization.'
          type: string
          example: pk_a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6
        id:
          $ref: '#/components/schemas/CommonProperties/properties/id'
        created:
          $ref: '#/components/schemas/CommonProperties/properties/created'
        updated:
          $ref: '#/components/schemas/CommonProperties/properties/updated'
        parent_plugin_id:
          description: 'If the product is an add-on then this is the ID of the parent product.'
          type: string
          format: int64
          minimum: 1
          example: '123456'
          nullable: true
        developer_id:
          description: 'The ID of the developer that owns the product.'
          type: string
          format: int64
          minimum: 1
          example: '123456'
          nullable: false
        store_id:
          description: 'The ID of the store that the product is being sold on.'
          type: string
          format: int64
          minimum: 1
          example: '123456'
          nullable: false
        slug:
          description: 'The `slug` of the product. If your plugin is listed on `WordPress.org` repository, use the exact slug.'
          type: string
          example: my-freemius-plugin
        title:
          description: 'The title of the product.'
          type: string
          example: 'My Freemius Plugin'
        environment:
          $ref: '#/components/schemas/CommonProperties/properties/environment'
        icon:
          description: 'Product''s icon (profile picture).'
          type: string
          example: 'https://img.freemius.com/plugin-icon-blue.png'
          nullable: true
        default_plan_id:
          description: 'Default plan ID of the product.'
          type: string
          format: int64
        plans:
          description: 'Comma separated, ordered plans collection.'
          type: string
          example: '123456,123457,123458'
        features:
          description: 'Comma separated, ordered features collection.'
          type: string
          example: '123456,123457,123458'
        money_back_period:
          description: 'Money-back guarantee in days.'
          type: integer
        refund_policy:
          $ref: '#/components/schemas/CommonEnums/properties/RefundPolicy'
        is_consumptive_usage:
          description: "Indicates whether the product follows a consumptive usage. Use this if your product includes one-off or consumptive usage like AI credits, API usage etc. It affects how the refund policy is generated for your product. Check our [documentation](help-documentation-selling-with-freemius-refund-policy.md) to learn more.\n\n> This is applicable for SaaS products only."
          type: boolean
        annual_renewals_discount:
          description: 'Renewals discount that will be applied to the chosen plan.'
          type: integer
          nullable: true
        renewals_discount_type:
          $ref: '#/components/schemas/CommonEnums/properties/RenewalsDiscountType'
        lifetime_license_proration_days:
          description: 'Number of days to allow proration when upgrading from one lifetime license to another. Can be a number greater than `30` or `null` for unlimited.'
          type: integer
          maximum: 65535
          minimum: 30
          example: 30
          nullable: true
        is_released:
          description: 'A flag that controls the visibility of add-ons in the in-dashboard add-ons marketplace. Defaults to true. Only applicable if the product is an add-on.'
          type: boolean
        is_sdk_required:
          description: 'A flag that controls whether the SDK should be required or not during deployment of a version. It defaults to `true`.'
          type: boolean
        is_pricing_visible:
          description: 'Determines if the pricing should be visible in the in-SDK pricing page. Defaults to true. Turn this off during the development of a new product.'
          type: boolean
        is_wp_org_compliant:
          description: 'Set to true if the free version of the module is hosted on WordPress.org. Defaults to true.'
          type: boolean
        installs_count:
          description: 'Total number of opted in sites which were logged with the SDK.'
          type: integer
        active_installs_count:
          description: 'Total number of active sites where the SDK is active.'
          type: integer
        free_releases_count:
          description: 'The number of "free" version of the product that were deployed from Freemius.'
          type: integer
        premium_releases_count:
          description: 'The number of "premium" version of the product that were deployed from Freemius.'
          type: integer
        total_purchases:
          description: 'Total number of payments recorded for the product.'
          type: integer
        total_subscriptions:
          description: 'Total number of subscriptions recorded for the product.'
          type: integer
        total_renewals:
          description: 'Total number of renewals recorded for the product.'
          type: integer
        total_failed_purchases:
          description: 'Total number of failed payments recorded for the product.'
          type: integer
          example: '1234'
        earnings:
          description: 'Total gross revenues.'
          type: number
          format: float
          example: '1234.56'
        type:
          $ref: '#/components/schemas/CommonEnums/properties/ProductType'
        type_alias:
          description: 'The alias type of the product. For example, ''extension'', ''chrome extension'', ''desktop app''.'
          type: string
        is_static:
          description: 'Determines whether the product is categorized as a static product (for example, a widget or a template).'
          type: boolean
      type: object
    PluginEmailAddress:
      title: ProductEmailAddress
      description: 'Represents the email address setup associated with the product.'
      properties:
        id:
          $ref: '#/components/schemas/CommonProperties/properties/id'
        created:
          $ref: '#/components/schemas/CommonProperties/properties/created'
        updated:
          $ref: '#/components/schemas/CommonProperties/properties/updated'
        plugin_id:
          $ref: '#/components/schemas/CommonProperties/properties/plugin_id'
        store_id:
          $ref: '#/components/parameters/store_id'
        general:
          description: 'The general system email address.'
          type: string
          example: foo@example.com
          nullable: true
        general_name:
          description: 'The label to the general system email address.'
          type: string
          example: 'Company Support'
          nullable: true
        dont_reply:
          description: 'The do-not-reply email address.'
          type: string
          example: donotreply@example.com
          nullable: true
        dont_reply_name:
          description: 'The label to the do-not-reply email address.'
          type: string
          example: 'Do Not Reply'
          nullable: true
        personal:
          description: 'The personal assistance email address.'
          type: string
          example: personalmanager@example.com
          nullable: true
        personal_name:
          description: 'The label to the personal assistance email address.'
          type: string
          example: 'John Doe'
          nullable: true
        personal_technical:
          description: 'The technical support representative email address.'
          type: string
          example: techsupport@example.com
          nullable: true
        personal_technical_name:
          description: 'The label to the technical support representative email address.'
          type: string
          example: 'Tech Support'
          nullable: true
        personal_setup:
          description: 'The happiness representative email address.'
          type: string
          example: support@example.com
          nullable: true
        personal_setup_name:
          description: 'The label to the happiness representative email address.'
          type: string
          example: Support
          nullable: true
        support:
          description: 'The general support email address.'
          type: string
          example: support@example.com
          nullable: true
        support_name:
          description: 'The label to the general support email address.'
          type: string
          example: Support
          nullable: true
      type: object
    PluginInfo:
      title: ProductInfo
      description: 'The basic information about a product.'
      properties:
        id:
          $ref: '#/components/schemas/CommonProperties/properties/id'
        created:
          $ref: '#/components/schemas/CommonProperties/properties/created'
        updated:
          $ref: '#/components/schemas/CommonProperties/properties/updated'
        plugin_id:
          $ref: '#/components/schemas/CommonProperties/properties/plugin_id'
        url:
          $ref: '#/components/schemas/CommonProperties/properties/url'
        description:
          description: 'The description of the product.'
          type: string
          example: 'Calculate profits for small to medium businesses. This product is a must-have for any business owner who intends to view the profits of their business. '
        short_description:
          description: 'The short description of the product.'
          type: string
          example: 'Calculate profits for small to medium businesses.'
        banner_url:
          $ref: '#/components/schemas/CommonProperties/properties/url'
        card_banner_url:
          $ref: '#/components/schemas/CommonProperties/properties/url'
        selling_point_0:
          description: 'The selling point one of the product.'
          type: string
          example: 'Ability to use stunning feature x.'
        selling_point_1:
          description: 'The selling point two of the product.'
          type: string
          example: 'Ability to use stunning feature y.'
        selling_point_2:
          description: 'The selling point three of the product.'
          type: string
          example: 'Ability to use stunning feature z.'
        screenshots:
          description: 'The URLs of the product screenshot.'
          type: object
          example:
            screenshot_0: 'https://exmaple.com/'
            screenshot_1: 'https://exmaple.com/'
            screenshot_2: 'https://exmaple.com/'
            screenshot_3: 'https://exmaple.com/'
          additionalProperties: true
      type: object
      x-internal: true
    PluginReview:
      title: ProductReview
      description: 'Represents a customer''s opinion after using a product. It can be generated by a real user or a developer. The review can be featured on the pricing page.'
      properties:
        id:
          $ref: '#/components/schemas/CommonProperties/properties/id'
        created:
          $ref: '#/components/schemas/CommonProperties/properties/created'
        updated:
          $ref: '#/components/schemas/CommonProperties/properties/updated'
        plugin_id:
          $ref: '#/components/schemas/CommonProperties/properties/plugin_id'
        external_id:
          description: 'The external ID of the review (in case migrating from another system).'
          type: string
        user_id:
          $ref: '#/components/schemas/CommonProperties/properties/user_id_nullable'
        rate:
          description: 'The score of the review.'
          type: integer
          maximum: 100
          minimum: 0
          example: 80
        title:
          description: 'The title of the review.'
          type: string
          example: 'Great plugin! It works perfectly.'
        text:
          description: 'The content of the review.'
          type: string
          example: 'I love this plugin! It has all the features I need and more. The support team is also very responsive and helpful. Highly recommend!'
        name:
          description: 'The full name of the reviewer.'
          type: string
          example: 'John Doe'
        job_title:
          description: 'The job title of the reviewer.'
          type: string
          example: 'Software Engineer'
        company:
          description: 'The company name of the reviewer.'
          type: string
          example: 'Example Software Inc.'
        company_url:
          $ref: '#/components/schemas/CommonProperties/properties/url'
        picture:
          $ref: '#/components/schemas/CommonProperties/properties/icon'
        profile_url:
          description: 'The URL of the reviewer''s profile.'
          type: string
          example: 'https://example.com/profile'
        license_id:
          $ref: '#/components/schemas/CommonProperties/properties/license_id'
        is_verified:
          description: 'Whether this is a genuine review generated by a real user.'
          type: boolean
          default: true
        is_featured:
          description: 'Whether the review should be included in marketing material (e.g. pricing page).'
          type: boolean
          default: false
      type: object
    PluginTag:
      title: ProductTag
      description: 'A product tag represents a version of the product that is available for download by users.'
      properties:
        id:
          $ref: '#/components/schemas/CommonProperties/properties/id'
        created:
          $ref: '#/components/schemas/CommonProperties/properties/created'
        updated:
          $ref: '#/components/schemas/CommonProperties/properties/updated'
        plugin_id:
          $ref: '#/components/schemas/CommonProperties/properties/plugin_id'
        developer_id:
          description: 'The ID of a developer.'
          type: string
          format: int64
          minimum: 1
          example: '1234'
        slug:
          description: 'The `slug` of the product. This is auto-generated from your product settings.'
          type: string
          example: my-freemius-plugin
          nullable: true
        premium_slug:
          description: 'The `slug` of the premium product. This is auto-generated from your product''s settings.'
          type: string
          example: my-freemius-plugin-pro
          nullable: true
        version:
          description: 'The version of the product. For WordPress.org products (plugins and themes), we recommend using semver semantics to support composer integration.'
          type: string
          format: semver
          example: 1.0.0
        sdk_version:
          description: 'The Freemius SDK version. Only relevant for WordPress products using the Freemius [WP SDK](help-documentation-wordpress-sdk.md).'
          type: string
          example: 1.2.2
        requires_platform_version:
          description: 'The platform version required (e.g WordPress version).'
          type: string
          example: 1.0.0
          nullable: true
        requires_programming_language_version:
          description: 'The programming language version (e.g PHP version).'
          type: string
          example: '5.6'
          nullable: true
        tested_up_to_version:
          description: 'The tested platform version that the product is compatible (e.g WordPress version).'
          type: string
          example: 1.0.0
          nullable: true
        downloaded:
          description: 'The number of times the product has been downloaded.'
          type: integer
          minimum: 0
          example: '1234'
        has_free:
          description: 'If the product has a free version.'
          type: boolean
        has_premium:
          description: 'If the product has a premium version.'
          type: boolean
        release_mode:
          description: 'The release mode of the product.'
          type: string
          enum:
            - released
            - pending
            - beta
        limit:
          description: 'The maximum number of downloads allowed for this version. This is used for [staged rollout](help-documentation-release-management-staged-rollouts.md) of WordPress products. Unlimited number is set as `null`.'
          type: integer
          minimum: 1
          example: 50
        uniques:
          description: 'The number of unique users that have downloaded the product.'
          type: integer
          minimum: 1
          example: '1234'
        is_incremental:
          description: 'Determines whether the version is incremental or not.'
          type: boolean
          example: true
      type: object
    Pricing:
      description: 'The pricing represents the cost of a quota and billing cycles of a plan.'
      properties:
        id:
          $ref: '#/components/schemas/CommonProperties/properties/id'
        created:
          $ref: '#/components/schemas/CommonProperties/properties/created'
        updated:
          $ref: '#/components/schemas/CommonProperties/properties/updated'
        currency:
          $ref: '#/components/schemas/CommonEnums/properties/Currency'
        plan_id:
          description: 'The ID of the plan.'
          type: string
          format: int64
          minimum: 1
          example: '1234'
        licenses:
          description: 'The number of activations or quota supported by the license that will be created through the pricing (Using [Freemius Checkout](help-documentation-selling-with-freemius-freemius-checkout-buy-button.md)). Use `null` for unlimited activations or quota.'
          type: integer
          example: '10'
          nullable: true
        monthly_price:
          description: 'The price for a single month.'
          type: number
          format: float
          example: '59.99'
          nullable: true
        annual_price:
          description: 'The price for one year.'
          type: number
          format: float
          example: '159.99'
          nullable: true
        lifetime_price:
          description: 'The lifetime price.'
          type: number
          format: float
          example: '359.99'
          nullable: true
        is_whitelabeled:
          description: 'Whether to [whitelabel](help-documentation-users-account-management-license-security.md#white_label_mode) the license that will be created from this pricing upon successful Checkout.'
          type: boolean
        is_hidden:
          description: 'Whether to hide the pricing from checkout and the pricing page in the WP dashboard.'
          type: boolean
      type: object
    Setting:
      description: 'Settings associated with an element.'
      properties:
        id:
          $ref: '#/components/schemas/CommonProperties/properties/id'
        created:
          $ref: '#/components/schemas/CommonProperties/properties/created'
        updated:
          $ref: '#/components/schemas/CommonProperties/properties/updated'
        setting_type:
          description: 'The type of the setting.'
          type: integer
        element_id:
          description: 'The ID of the element the setting is associated with.'
          type: string
          format: int64
          minimum: 1
          example: '1234'
        element_type:
          description: 'The type of the element. It is unique for each entity type.'
          type: integer
        data:
          description: 'JSON encoded data of the settings.'
          type: string
          format: json
          example: '{"key":"value"}'
      type: object
      x-internal: true
    Subscription:
      description: 'A subscription is created when a user uses [Freemius Checkout](checkout.md) to purchase or subscribe to a plan of a product.'
      properties:
        user_id:
          $ref: '#/components/schemas/CommonProperties/properties/user_id'
        install_id:
          $ref: '#/components/schemas/CommonProperties/properties/install_id_nullable'
        plan_id:
          $ref: '#/components/schemas/CommonProperties/properties/plan_id'
        pricing_id:
          $ref: '#/components/schemas/CommonProperties/properties/pricing_id'
        license_id:
          $ref: '#/components/schemas/CommonProperties/properties/license_id'
        ip:
          $ref: '#/components/schemas/CommonProperties/properties/ip_nullable'
        country_code:
          $ref: '#/components/schemas/CommonProperties/properties/country_code'
        zip_postal_code:
          $ref: '#/components/schemas/CommonProperties/properties/zip_postal_code_nullable'
        vat_id:
          $ref: '#/components/schemas/CommonProperties/properties/vat_id_nullable'
        coupon_id:
          $ref: '#/components/schemas/CommonProperties/properties/coupon_id_nullable'
        user_card_id:
          description: 'The ID of the user card that was used for this payment.'
          type: string
          format: int64
          example: '12345'
        source:
          $ref: '#/components/schemas/Migration/properties/source'
        plugin_id:
          $ref: '#/components/schemas/CommonProperties/properties/plugin_id'
        external_id:
          description: 'The external ID of the gateway entity.'
          type: string
          example: abcde12345
        gateway:
          description: 'The gateway used for the purchase. The gateway will be set to `null` when purchasing a product with a 100% discount.'
          type: string
          nullable: true
        environment:
          $ref: '#/components/schemas/CommonProperties/properties/environment'
        id:
          $ref: '#/components/schemas/CommonProperties/properties/id'
        created:
          $ref: '#/components/schemas/CommonProperties/properties/created'
        updated:
          $ref: '#/components/schemas/CommonProperties/properties/updated'
        currency:
          $ref: '#/components/schemas/CommonEnums/properties/Currency'
        tax_rate:
          description: 'The tax rate as a fraction. It will either be US sales tax or VAT.'
          type: number
          format: float
          minimum: 0
          example: '1.00'
        total_gross:
          description: 'The total gross amount of the subscription, including taxes.'
          type: number
          format: float
          minimum: 0
          example: '1.21'
        amount_per_cycle:
          description: 'The plan''s original amount per cycle (not including taxes).'
          type: number
          format: float
          minimum: 0
          example: '1.00'
        initial_amount:
          description: 'The initial payment amount (not including taxes).'
          type: number
          format: float
          minimum: 0
          example: '1.00'
        renewal_amount:
          description: 'The renewals amount (not including taxes).'
          type: number
          format: float
          minimum: 0
          example: '1.00'
        renewals_discount:
          description: 'The renewals discount that will be applied to the chosen plan.'
          type: integer
          minimum: 0
          example: '1'
        renewals_discount_type:
          $ref: '#/components/schemas/CommonEnums/properties/RenewalsDiscountType'
        billing_cycle:
          $ref: '#/components/schemas/CommonEnums/properties/BillingCycle'
        outstanding_balance:
          description: 'Any outstanding balance that the user has for this subscription.'
          type: number
          format: float
          minimum: 0
          example: '1.00'
        failed_payments:
          description: 'Number of failed payments associated with the subscription.'
          type: integer
          minimum: 0
          example: '1'
        trial_ends:
          description: 'The date time when the trial period ends. If `null` the subscription is not associated with a trial.'
          type: string
          format: date-time
          example: '2025-01-01 00:00:00'
          nullable: true
        next_payment:
          description: 'Datetime of the next payment, or `null` if cancelled.'
          type: string
          format: date-time
          example: '2025-01-01 00:00:00'
          nullable: true
        canceled_at:
          description: 'Datetime of the cancellation.'
          type: string
          format: date-time
          example: '2025-01-01 00:00:00'
          nullable: true
      type: object
    Trial:
      description: 'A trial represents a user''s trial period for a product. Please read our [documentation](help-documentation-selling-with-freemius-free-trials.md) to learn more about trials.'
      properties:
        id:
          $ref: '#/components/schemas/CommonProperties/properties/id'
        created:
          $ref: '#/components/schemas/CommonProperties/properties/created'
        updated:
          $ref: '#/components/schemas/CommonProperties/properties/updated'
        plugin_id:
          $ref: '#/components/schemas/CommonProperties/properties/plugin_id'
        user_id:
          $ref: '#/components/schemas/CommonProperties/properties/user_id'
        payment_id:
          $ref: '#/components/schemas/CommonProperties/properties/payment_id_nullable'
        subscription_id:
          $ref: '#/components/schemas/CommonProperties/properties/subscription_id_nullable'
        license_id:
          $ref: '#/components/schemas/CommonProperties/properties/license_id_nullable'
        trial_ends_at:
          description: 'The date and time the trial ends, under UTC timezone.'
          type: string
          format: date-time
          example: '2025-01-01 00:00:00'
          nullable: false
        with_payment_method:
          description: 'Whether the trial was created with a payment method. Freemius supports both free and paid trials.'
          type: boolean
        canceled_at:
          description: 'The date and time the trial was cancelled, under UTC timezone. If `null` the trial has not been cancelled.'
          type: string
          format: date-time
          example: '2025-01-01 00:00:00'
          nullable: true
        converted_at:
          description: "The date and time the trial was converted to a paid subscription or one-time purchase, under UTC timezone.\nIf `null` the trial has not been converted."
          type: string
          format: date-time
          example: '2025-01-01 00:00:00'
          nullable: true
        environment:
          $ref: '#/components/schemas/CommonProperties/properties/environment'
      type: object
    Uninstall:
      description: 'An uninstall represents a user uninstalling a product from their site. This is different from deleting.'
      properties:
        id:
          $ref: '#/components/schemas/CommonProperties/properties/id'
        created:
          $ref: '#/components/schemas/CommonProperties/properties/created'
        updated:
          $ref: '#/components/schemas/CommonProperties/properties/updated'
        plugin_id:
          $ref: '#/components/schemas/CommonProperties/properties/plugin_id'
        install_id:
          $ref: '#/components/schemas/CommonProperties/properties/install_id'
        site_id:
          description: 'The ID of the site.'
          type: string
          format: int64
          minimum: 1
          example: '1234'
        reason_id:
          description: "\nUninstall reason. Possible values:\n\n* `1` - No longer needed\n* `2` - Found a better alternative\n* `3` - Only needed for short period\n* `4` - Broke the website\n* `5` - Suddenly stopped working\n* `6` - Cannot continue paying\n* `7` - Other\n* `8` - Didn't work after installation\n* `9` - User doesn't like to share data\n* `10` - Didn't understand how it works\n* `11` - Missing specific feature\n* `12` - Didn't work\n* `13` - Expected something else\n* `14` - Expected to work differently\n* `15` - Temporary deactivation\n        "
          type: integer
          enum:
            - 1
            - 2
            - 3
            - 4
            - 5
            - 6
            - 7
            - 8
            - 9
            - 10
            - 11
            - 12
            - 13
            - 14
            - 15
          example: 1
        reason_info:
          description: 'Additional information gathered from the user for the uninstallation. This is populated when the product user chooses “Other” in contrast to pre-set options.'
          type: string
      type: object
    User:
      description: 'A **User** is a person who is registered to Freemius through some usage of one or more products selling through Freemius. The user could own licenses of such products or simply could have been linked to the Free version of the products. Every user has unique email address.'
      properties:
        note:
          description: 'A note about the user. Only visible to the developer.'
          type: string
        is_marketing_allowed:
          description: 'Whether or not the user has given their consent for marketing materials. A `null` value indicates that the user has not made a decision yet.'
          type: boolean
          nullable: true
        is_beta:
          description: 'Whether or not the user has opted-in to beta versions. We do not recommend using this option anymore since it will opt-in the user to all sites/activations. Currently, sites or activations can be managed individually.'
          type: boolean
        email:
          description: 'Email address of the person.'
          type: string
          example: jane@example.com
        first:
          description: 'First name of the person.'
          type: string
          example: Jane
        last:
          description: 'Last name of the person.'
          type: string
          example: Doe
        picture:
          description: 'Profile picture URL.'
          type: string
          example: 'https://example.com/profile-pic.jpg'
        ip:
          description: 'The IP address (v4 or v6).'
          type: string
          format: ipv4|ipv6
          example: 127.0.0.1
          nullable: true
        is_verified:
          description: 'Whether the person is trusted or not.'
          type: boolean
          example: 'true'
        auth:
          $ref: '#/components/schemas/CommonEnums/properties/AuthenticationType'
        secret_key:
          description: 'The secret key associated with the entity for authorization.'
          type: string
          example: sk_a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6
        public_key:
          description: 'The public key associated with the entity for authorization.'
          type: string
          example: pk_a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6
        id:
          $ref: '#/components/schemas/CommonProperties/properties/id'
        created:
          $ref: '#/components/schemas/CommonProperties/properties/created'
        updated:
          $ref: '#/components/schemas/CommonProperties/properties/updated'
        gross:
          description: 'The total amount of money the user has spent on the platform.'
          type: number
          format: float
        last_login_at:
          description: 'Date and time of the last login.'
          type: string
          format: date-time
          example: '2025-07-30 05:56:29'
          nullable: true
        email_status:
          $ref: '#/components/schemas/CommonEnums/properties/EmailStatus'
      type: object
    UserPluginEnriched:
      type: object
      allOf:
        -
          $ref: '#/components/schemas/User'
        -
          properties:
            plugin_id:
              $ref: '#/components/schemas/CommonProperties/properties/plugin_id'
            user_id:
              $ref: '#/components/schemas/CommonProperties/properties/user_id'
            gross:
              description: 'Gross payments made by the user for the product'
              type: number
              format: float
              example: 999
            is_marketing_allowed:
              description: 'Whether the user has consented for marketing notifications.'
              type: boolean
          type: object
    Affiliate:
      description: 'An affiliate is individual or businesses that promotes and sells products or services in exchange for a commission on each sale.'
      properties:
        id:
          $ref: '#/components/schemas/CommonProperties/properties/id'
        created:
          $ref: '#/components/schemas/CommonProperties/properties/created'
        updated:
          $ref: '#/components/schemas/CommonProperties/properties/updated'
        user_id:
          $ref: '#/components/schemas/CommonProperties/properties/user_id'
        ip:
          $ref: '#/components/schemas/CommonProperties/properties/ip'
        paypal_email:
          description: 'The PayPal email for payout purposes.'
          type: string
          example: foo@freemius.com
        plugin_id:
          $ref: '#/components/schemas/CommonProperties/properties/plugin_id'
        affiliate_terms_id:
          description: 'The ID of the affiliate terms.'
          type: string
          format: int64
          minimum: 1
          example: '1234'
        custom_affiliate_terms_id:
          description: 'The ID of the custom affiliate terms.'
          type: string
          format: int64
          minimum: 1
          example: '1234'
        is_using_custom_terms:
          description: 'Whether the affiliate is using custom terms.'
          type: boolean
        status:
          description: 'The status of the affiliate signup.'
          type: string
          default: '\Freemius\Entities\Affiliation\Affiliate::STATE_PENDING'
          enum:
            - pending
            - rejected
            - suspended
            - active
        domain:
          description: 'The domain of the affiliate.'
          type: string
          example: 'https://awesome-products.com'
        earnings:
          description: 'The earnings of the affiliate from sales.'
          type: number
          format: float
          minimum: 0
          example: '2000.45'
        pending_referrals:
          description: 'The number of unapproved/pending referrals.'
          type: number
          minimum: 1
          example: '1234'
        visits:
          description: 'The number of visits through the affiliate link.'
          type: integer
          minimum: 1
          example: '1234'
        unique_visits:
          description: 'The number of unique visits through the affiliate link.'
          type: integer
          minimum: 1
          example: '1234'
      type: object
    AuthToken:
      properties:
        access:
          description: 'The access token that our API or general infrastructure will accept.'
          type: string
          example: 1234567890abcdef1234567890abcdef
        expires:
          description: 'The expiration time of the access token in timestamp.'
          type: integer
          example: '1234567890'
        refresh:
          description: 'The refresh token which can be used to generate a new access token. We don''t support creating access tokens with refresh tokens anymore. For API communication please use the Bearer token.'
          type: string
          example: '"1234567890abcdef1234567890abcdef"'
          deprecated: true
      type: object
      x-internal: true
    FSEndpointDeveloperPluginPricing:
      description: 'The key represents the ID of the plan'
      properties:
        monthly_price:
          description: 'Monthly pricing in different currencies'
          properties:
            usd:
              type: number
              format: float
              example: 9.99
            gbp:
              type: number
              format: float
              example: 7.99
            eur:
              type: number
              format: float
              example: 8.99
          type: object
        annual_price:
          description: 'Annual pricing in different currencies'
          properties:
            usd:
              type: number
              format: float
              example: 99.99
            gbp:
              type: number
              format: float
              example: 79.99
            eur:
              type: number
              format: float
              example: 89.99
          type: object
        lifetime_price:
          description: 'Lifetime pricing in different currencies'
          properties:
            usd:
              type: number
              format: float
              example: 299.99
            gbp:
              type: number
              format: float
              example: 249.99
            eur:
              type: number
              format: float
              example: 279.99
          type: object
      type: object
    FSEndpointDeveloperPluginSubscriptions:
      type: array
      items:
        $ref: '#/components/schemas/Discount'
    FSEndpointDeveloperPluginUserSubscriptions:
      type: array
      items:
        $ref: '#/components/schemas/Discount'
  responses:
    '204':
      description: 'The API has no content to send. This usually happens when some entity is deleted.'
    '400':
      description: 'Bad request. The request could not be understood by the server due to malformed syntax or arguments.'
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ApiError'
    '401':
      description: 'Unauthorized access error. The request requires [authentication](https://freemius.com/help/api/#bearer-token-authentication) but was not provided or the provided authentication does not satisfy the required permissions.'
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ApiError'
    '402':
      description: 'The request is missing the specified argument.'
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ApiError'
    '404':
      description: 'The requested resource was not found.'
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ApiError'
  parameters:
    developer_id:
      name: developer_id
      in: path
      description: 'The ID of the developer.'
      required: true
      schema:
        type: integer
        format: int64
        minimum: 1
      example: '1234'
    store_id:
      name: store_id
      in: path
      description: 'The ID of the store.'
      required: true
      schema:
        type: integer
        format: int64
        minimum: 1
      example: '1234'
    plugin_id:
      name: plugin_id
      in: path
      description: 'The ID of the product.'
      required: true
      schema:
        type: integer
        format: int64
        minimum: 1
      example: '1234'
    product_id:
      name: product_id
      in: path
      description: 'The ID of the product.'
      required: true
      schema:
        type: integer
        format: int64
        minimum: 1
      example: '1234'
    bank_account_id:
      name: bank_account_id
      in: path
      description: 'The ID of the bank account.'
      required: true
      schema:
        type: integer
        format: int64
        minimum: 1
      example: '1234'
    cart_id:
      name: cart_id
      in: path
      description: 'The ID of the Cart.'
      required: true
      schema:
        type: integer
        format: int64
        minimum: 1
      example: '1234'
    setting_id:
      name: setting_id
      in: path
      description: 'The ID of the setting.'
      required: true
      schema:
        type: integer
        format: int64
        minimum: 1
      example: '1234'
    payment_id:
      name: payment_id
      in: path
      description: 'The ID of the payment.'
      required: true
      schema:
        type: integer
        format: int64
        minimum: 1
      example: '1234'
    install_id:
      name: install_id
      in: path
      description: 'The ID of the install.'
      required: true
      schema:
        type: integer
        format: int64
        minimum: 1
      example: '1234'
    clone_id:
      name: clone_id
      in: path
      description: 'The ID of the clone.'
      required: true
      schema:
        type: integer
        format: int64
        minimum: 1
      example: '1234'
    plan_id:
      name: plan_id
      in: path
      description: 'The ID of the plan.'
      required: true
      schema:
        type: integer
        format: int64
        minimum: 1
      example: '1234'
    license_id:
      name: license_id
      in: path
      description: 'The ID of the License.'
      required: true
      schema:
        type: integer
        format: int64
        minimum: 1
      example: '1234'
    user_id:
      name: user_id
      in: path
      description: 'The ID of the User.'
      required: true
      schema:
        type: integer
        format: int64
        minimum: 1
      example: '1234'
    subscription_id:
      name: subscription_id
      in: path
      description: 'The ID of the Subscription.'
      required: true
      schema:
        type: integer
        format: int64
        minimum: 1
      example: '1234'
    pricing_id:
      name: pricing_id
      in: path
      description: 'The ID of the Pricing.'
      required: true
      schema:
        type: integer
        format: int64
        minimum: 1
      example: '1234'
    addon_id:
      name: addon_id
      in: path
      description: 'The ID of the Addon.'
      required: true
      schema:
        type: integer
        format: int64
        minimum: 1
      example: '1234'
    tag_id:
      name: tag_id
      in: path
      description: 'The ID of the product version.'
      required: true
      schema:
        type: integer
        format: int64
        minimum: 1
      example: '1234'
    coupon_id:
      name: coupon_id
      in: path
      description: 'The ID of the coupon.'
      required: true
      schema:
        type: integer
        format: int64
        minimum: 1
      example: '1234'
    special_id:
      name: special_id
      in: path
      description: 'The ID of the special coupon.'
      required: true
      schema:
        type: string
        enum:
          - affiliate
          - cart_recovery
          - subscription_cancellation
          - exit_intent
          - renewals_discount
          - manual_renewals_discount
      example: cart_recovery
    review_id:
      name: review_id
      in: path
      description: 'The ID of the review.'
      required: true
      schema:
        type: integer
        format: int64
        minimum: 1
      example: '1234'
    feature_id:
      name: feature_id
      in: path
      description: 'The ID of the feature.'
      required: true
      schema:
        type: integer
        format: int64
        minimum: 1
      example: '1234'
    event_id:
      name: event_id
      in: path
      description: 'The ID of the event.'
      required: true
      schema:
        type: integer
        format: int64
        minimum: 1
      example: '1234'
    fields:
      name: fields
      in: query
      description: 'Comma separated list of fields to return in the response. If not specified, all fields are returned.'
      required: false
      schema:
        type: string
      example: 'id,name,slug'
    count:
      name: count
      in: query
      description: 'The number of records to return.'
      required: false
      schema:
        type: integer
        default: 25
        maximum: 50
        minimum: 1
      example: '10'
    offset:
      name: offset
      in: query
      description: 'The number of records to skip before starting to return records. Default is 0.'
      required: false
      schema:
        type: integer
        default: 0
        minimum: 0
      example: '10'
    gateway:
      name: gateway
      in: query
      description: 'Filter by gateway.'
      required: false
      schema:
        type: string
        enum:
          - paypal
          - stripe
      example: stripe
    from:
      name: from
      in: query
      description: 'The start of the date range in YYYY-MM-DD HH:MM:SS format'
      required: false
      schema:
        type: string
        format: date-time
      example: '2025-08-01 00:00:00'
    to:
      name: to
      in: query
      description: 'The end of the date range in YYYY-MM-DD HH:MM:SS format'
      required: false
      schema:
        type: string
        format: date-time
      example: '2025-08-01 00:00:00'
    billing_cycle:
      name: billing_cycle
      in: query
      description: 'Filter by billing cycle.'
      required: false
      schema:
        $ref: '#/components/schemas/CommonEnums/properties/BillingCycle'
    uid:
      name: uid
      in: query
      description: 'The Unique identifier. It is a 32 characters long string.'
      required: true
      schema:
        type: string
        format: uid
        maxLength: 32
        minLength: 32
  securitySchemes:
    ApiAuthBearer:
      type: http
      description: "\nThe access token you generated for the scope entity. The token has a format `Bearer {API_Key}`. You can get the API Key from the [Freemius Developer Dashboard](https://dashboard.freemius.com) for a product or a store.\n\n### Retrieving an API Key\n\n1. Go to the [Freemius Developer Dashboard](https://dashboard.freemius.com/).\n2. Open the Settings page of the relevant product.\n3. Click the API & Keys tab.\n4. Copy the API Bearer Authorization Token from the UI.\n\nTo regenerate the API Key you will need to regenerate the secret key of the product or the store. This can be done from the `Information` tab of the `Settings` page.\n\nYou will also need the product ID for all API endpoints. It can be found from the **Keys** section under the `Information` tab of the `Settings` page.\n"
      bearerFormat: AccessToken
      scheme: bearer
    ApiAuthFSAHeader:
      type: apiKey
      description: "\nThe token starts with \"`FSA {scope_entity_id}:{access_token}`\" and must be present in the header `Authorization`.\n\n> This is supported for the developer scope entity only at the moment.\n\nYou must call the login endpoint to automatically generate and store the cookie.\n"
      name: Authorization
      in: header
      x-remove-from-doc: true
    ApiAuthFSACookie:
      type: apiKey
      description: "\nThe token starts with \"`FSA {scope_entity_id}:{access_token}`\" and must be present in an `httpOnly` cookie named `fsa_access_token`.\n\n> This is supported for the developer scope entity only at the moment.\n\nYou must call the login endpoint to automatically generate and store the cookie.\n"
      name: fsa_access_token
      in: cookie
      x-remove-from-doc: true
security:
  -
    ApiAuthBearer: []
tags:
  -
    name: Products
    description: 'All operations which can be done on a product.'
  -
    name: Developers
    description: 'All operations which can be done from on a developer.'
    x-remove-from-doc: true
  -
    name: Subscriptions
    description: 'All operations associated to a subscription.'
  -
    name: Users
    description: 'All operations which can be done on a user belonging to a store or a product.'
  -
    name: Licenses
    description: 'All operations which can be done on a license belonging to a store or a product.'
  -
    name: Coupons
    description: 'All operations which can be done on a coupon belonging to a store or a product.'
  -
    name: Carts
    description: 'All operations which can be done on a cart belonging to a store or a product.'
  -
    name: Payments
    description: 'All operations associated to a payment.'
  -
    name: Installations
    description: 'Operations related to the installation of a product.'
  -
    name: Trials
    description: 'Operations related to a trial license of a product.'
  -
    name: Addons
    description: 'Operations related to an addon of a product.'
  -
    name: Plans
    description: 'Operations related to plans, pricings and features of a product.'
  -
    name: Events
    description: 'Operations related to events of a store or product.'
  -
    name: Reviews
    description: 'Operations related to reviews of a product.'
  -
    name: Deployments
    description: 'Operations related to version deployments and retrieval.'
externalDocs:
  description: 'Browse Tutorials and Guides.'
  url: 'https://freemius.com/help/documentation/'
