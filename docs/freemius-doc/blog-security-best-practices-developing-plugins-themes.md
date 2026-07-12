As a WordPress developer, there are many decisions you have to make about what to work on. Your primary interest and priority are to build an amazing theme or plugin, and security measures often take a backseat when you get in the driver’s seat to work on the code. When was the last time you sat down and reviewed your own code for security issues? No, I didn’t think so 😉

These tips are based on my experience from both developing plugins at [CleverPlugins](https://cleverplugins.com/) and helping countless customers get their websites back online after being hacked. Developing a security plugin like [WP Security Ninja](https://wpsecurityninja.com/) has not made me any less paranoid about other people’s code.

The most common reason for hacked websites is still lousy password management, but that should not be an excuse to use some of the simple ways you can protect your code.

When you develop a plugin or theme, you want it to become popular and have it installed on as many websites as possible. The bigger your success, the bigger the chance people will try to abuse your work to hack your users’ websites.

Due to the popularity of WordPress, it has become one of the most common targets for hackers. If a vulnerability is detected in a plugin or a theme, it can mean thousands, if not hundreds of thousands of websites are open for abuse.

Unfortunately, it happens regularly that a vulnerability appears in a well-known product, so it is worth taking some basic security measures to protect your code for your users.

### What About the WordPress.org Review Team?

You might think that the team that reviews plugins and themes before publishing on the official repository checks for all [kinds of security issues](https://developer.wordpress.org/plugins/security/), but the team is tiny and consists only of a few people. The queue of plugins and themes to check is continuously growing, so the time they have to review each is limited.

However, if they do find something, they might [automatically close your plugin](https://developer.wordpress.org/plugins/wordpress-org/plugin-security/) until you fix it or email you a warning that you must fix a vulnerability before a certain timeframe.

The point is that once your plugin or theme is listed on the repository, you can push out updates via the repository without additional screening, so a vulnerability can easily sneak in anytime and go undetected for almost any period of time.

Basically, tightening up your plugin security measures is up to you, so let’s look at some ways you can protect your WordPress product and prevent yourself from a lot of headaches and potentially a negative impact on your brand.

Here’s what you can do to securely develop your WordPress plugin or theme.

## 1. Think about security from all perspectives!

You never know who might be using your plugin or theme and what level of understanding they have about security, if any at all.

Administrators, editors, or regular users on any customer website might not use secure passwords, and their accounts could be hacked. If your product is not secured, these accounts could be abused to gain further access to install malicious code on your customer’s website.

You should not expect the server administrators that have configured the server that the website runs on to know enough about how to protect your website from other sites on the same server. If the website is hosted by a big provider, you can expect the website to be properly “separated”, but you do not know where your product will be installed.

Does that sound paranoid? Maybe. But, if and when your plugin or theme becomes super popular, you will be happy to have taken a paranoid approach to security.

## 2. Prevent XSS – Cross-Site Scripting attacks

This one is getting more and more important as WordPress is becoming a more frontend driven project with Gutenberg and ReactJS.

One of the most common mistakes for WordPress developers is forgetting to validate and sanitize their code – leaving it open to XSS attacks. There are a couple of variations of XSS, but in general, an XSS attack occurs when a hacker is allowed to inject code into the server and then have it execute in a visitor’s browser.

Imagine you have an input field. For simplicity’s sake, let’s say it’s a comment field where users or visitors can submit a comment to a post.

A hacker will attempt to submit a comment with `"<script>alert('XSS');</script>"`.

Now, this is just a basic example that pops up an alert on the user’s screen and nothing else. An actual hacker will use the comment field to inject code that loads code from their site that can steal information from the visitor’s browser and much more.

We can prevent this from happening with validating, sanitizing, and escaping.

**Validating** is checking the data submitted before doing anything, such as storing it in the database. Whenever data is submitted, you can check it and make sure it is acceptable. If it is a quantity field, you expect a number. If it is not a number, you can return an error message to the user. 

**Sanitizing** data is processing the submitted information and making sure it does not contain anything we do not want to store, such as removing any unwanted characters. WordPress has several functions built in to help with this. More on sanitizing in a bit.

**Escaping** is preventing any malicious code from actually executing in your browser. Let’s say you already have malicious code injected into your website, or another plugin or theme is letting hackers insert code into the data that you are using – escaping the data to the screen before showing it will prevent it from being a problem. 

Let’s look at the same simple example as we used before `"<script>alert('XSS');</script>"`

If we do not do anything with this code, the browser will think it is HTML code. The important detail here is the &lt; &gt; characters that are used to define HTML tags. By escaping these, we turn `<` into `&lt;` and `>` into `&gt;` The browser now understands that this is not actual HTML code, and it should just show a less-than and greater-than sign instead.

By validating, sanitizing, and escaping all data that goes in and out of your application, you are protecting your users from one of the most common attack methods.

## 3. Be careful about SQL injections

As the name implies, an attacker can use SQL injections to make your website process a tweaked SQL query and use that to gain access to your database.

Depending on the data you store on your website, having your website data leaked from an SQL injection attack could go from being embarrassing to completely devastating your reputation and business.

SQL injection is an old way to attack a website, but it is still very effective and there are many people looking for ways to use this form of attack. In October 2020, the popular Loginizer WordPress plugin [announced they had an SQL injection vulnerability](https://www.zdnet.com/article/wordpress-deploys-forced-security-update-for-dangerous-bug-in-popular-plugin/) that left over a million websites at risk.

In 2019, unknown hackers [stole millions of Bulgarians’ tax data](https://en.wikipedia.org/wiki/2019_Bulgarian_revenue_agency_hack) via an SQL injection attack, and in 2016, a group of Russian hackers [extracted voter information](https://abc7chicago.com/russia-russian-intelligence-hacking-2016-election/3758586/) of about 500,000 people in Ohio. These kinds of attacks are still very effective, and you can find lots of information about them.

![Comic Strip about Sanitizing Data Inputs](https://freemius.com/blog/wp-content/uploads/2020/11/comic-strip-about-sanitizing-data-inputs-2.png)

Source: [https://xkcd.com/327/](https://xkcd.com/327/)

The most common place an SQL injection happens is in a form field that accepts user input – for example, a name. The attack happens by entering parts of SQL code in the input fields, creating a custom query giving a different result than what you would expect.

Let’s say you have a form that allows people to search for a particular name.

`SELECT * FROM wp_postmeta WHERE meta_value = 'Henry' AND meta_key = 'celebrity_name';`

This simple example would pick up all rows from the post meta table with all rows that have the name `Henry` and a specific key, `celebrity_name` – this way, we do not return the entire database and only the particular rows we need.

An attacker would attempt to parse a different value – for example `’Henry' OR 1=1--`

The query will now return all rows with our specific value, or anything else – since `OR 1=1` in SQL is always true.

It gets worse, though. Our SQL query only asked for results where the `meta_key` matches the particular value we are looking for, so we would not return everything. This should limit the impact the SQL injection attack has, right?

Well, not so. In SQL, the double-dash is a comment indicator, so everything that comes after this is commented.

`SELECT * FROM wp_postmeta WHERE meta_value = 'Henry' OR 1=1--' AND meta_key = 'celebrity_name';`

This means the query looks like this:

`SELECT * FROM wp_postmeta WHERE meta_value = 'Henry' OR 1=1`

The query now essentially returns everything in that database table.

This was just a simple example. There are many more complicated ways to access most, if not all, the information in a database. An attacker would be able to try blind SQL injection attacks, which means running code on your database – adding a new administrator, removing all your data, and so on.

Most attacks would be in the form of just random query strings containing parts of SQL submitted to your website forms. The automated scripts would detect any changes to your website output and then detect the potential for attack.

A simple, effective way is to send an apostrophe `'` as input and see if it changes anything, an error occurs, or more results are returned.

### WordPress to the rescue

Instead of interacting directly with the database, any developer should use the built-in database abstraction class in WordPress, `$wpdb`.

The `$wpdb` class in WordPress has all the CRUD functionality you need to interact with the database safely, and you can even use the class to interact with your own database tables if your plugin or theme needs to.

You can solve the problem by anticipating what kind of data should be reasonably entered in each input form. In our previous example, we searched for a name. We could sanitize the input to ensure we only accept letters. If you have a select box or radio group that only contains a few options, you can check the data to make sure it is only one of the choices you allow.

The most important thing you can do to solve the problem is prepare your data with the `$wpdb->prepare()` function.

This function takes a prepared query string and an array of the arguments you want to be added to the SQL query.

```
$meta_key = 'celebrity_name';
$meta_val = 'Henry'
$allhenrys = $wpdb->get_results(
  $wpdb->prepare(
    "SELECT * FROM $wpdb-&gt;postmeta WHERE meta_key = %s AND meta_value = %s",
    $meta_key,
    $meta_val
  )
);
```

All the work takes place inside the `prepare()` function. The first parameter, the prepared query – contains the placeholder `%s` instead of the actual values. This is replaced by the other parsed variables, `$meta_key` and `$meta_val`.

Note – It is important not to have an apostrophe in your query surrounding the placeholders, as the function will add those for you.

This is a simplified example, but the same process can be used for any database query and you can use `%s` for strings, `%d` for integers and `%f` for floats.

There are also functions for specific situations, such as adding a new row to the database. For this purpose you can use `$wpdb->insert()`.

```
$wpdb->insert(
  "{$wpdb->prefix}my_custom_table",
  array(
    'name'   => 'Henry',
    'userid' => 123,
    'score'  => 10,
  ),
  array(
    '%s',
    '%d',
    '%d',
  )
);
```

Using the prepare function can help prevent the majority of SQL injection attempts against your product.

Please remember to check the [$wpdb documentation](https://developer.wordpress.org/reference/classes/wpdb/). Some functions will escape input for you; others expect you to escape the input yourself before parsing the data to the function.

## 4. Use nonces to protect your requests

Using the [nonce system in WordPress](https://codex.wordpress.org/WordPress_Nonces) can help you prevent many attacks. A nonce in terms of security is a number used only once. The idea is to add this unique number to all requests you make from your code to the WordPress install as a way to verify that this request is legit.

It is a little bit like having a secret password you need to give to the bouncer to get into a club 🙂

However, nonces in WordPress are a little different – they are neither a number nor is the nonce used only once.

Technically the nonces in WordPress can contain both lowercase letters and numbers, and instead of it being used only *once*, it is regenerated after a period of time.

The way you use a nonce is that the PHP code that registers your JavaScript files generates a little unique combination of numbers and letters and parses that along so your JS code can read it.

Every time the JavaScript code sends a request to your website, it sends along that piece of code, and if the code does not match, your code should ignore the request completely.

It is always a little easier with an example, so let’s see a simple way to load a .js file in your plugin following these steps:

#### Using nonces in a WordPress plugin

```
add_action('wp_enqueue_scripts', 'load_my_plugin_script');

function load_my_plugin_script() {
  // Register the script with all details and ensures it is loaded after jQuery
  wp_register_script('secure-plugin', plugin_dir_url( __FILE__ ). 'js/secure-plugin.js', array( 'jquery' ) );

  // Here happens the magic, we add some details to an object that we can later reference and read from in our JS code.
  wp_localize_script(
    'secure-plugin',
    'plugin_ajax_object',
    array(
      'nonce' => wp_create_nonce('secure-plugin-nonce')
    )
  );

  // Once that is done, we can now enqueue the script
  wp_enqueue_script('secure-plugin');
}
```

In this function, we tell WordPress to load a JavaScript file. First, we register the file we want to load with `wp_register_script()`.

Then we use `wp_localize_script()` to parse an array of data, in particular “nonce” that contains the unique nonce that we want to use in our JS code. Remember, you can send all kinds of other information in that array too, but we are just keeping it simple in this example.

When you send a request from your JavaScript file, you need to include that unique nonce. Doing that is easy:

#### Using nonce from WordPress plugin in a JavaScript file

```
jQuery(document).ready(function($) {
  $.ajax({
    url: ajaxurl, // WP variable, contains URL pointing to admin-ajax.php
    type: 'POST',
    data: {
      'action':      'get_custom_data',
      '_ajax_nonce': plugin_ajax_object.nonce,
      'user_data':   'Some input from a user'
    },
    success: function( response ) {
      // Here we do what happens if all is good - update the interface with a success message!?
    },
    error: function( response ) {
      // Whooops, something went wrong!
      // console.log(response);
    }
  });
});
```

Since we used `wp_localize_script()` we can use the plugin\_ajax\_object variable in JavaScript. We send the nonce as a variable, `_ajax_nonce`.

#### Check and verify a nonce in a WordPress plugin from JavaScript code

```
add_action('wp_ajax_get_custom_data', 'get_custom_data');

function get_custom_data() {
  // Ready for the magic to protect your code?
  check_ajax_referer('secure-plugin-nonce');

  /**
   * That's it - the check_ajax_referer function verifies the nonce is correct or it dies and stops code execution if it fails.
   *
   * If you want to customize the error handling and perhaps return an error to your JS code, you could change the code to something like:
   * if ( ! check_ajax_referer( 'secure-plugin-nonce', false, false ) ) {    
   *   wp_send_json_error( 'Invalid nonce' );
   * }
   */

  $sanitized_user_data = sanitize_text_field( $_POST['user_data'] );

  // ... continue with the rest of your plugin's function code ...
}
```

The magic happens with the function `check_ajax_referer()` that checks the nonce and simply fails and stops any further code execution if the nonce does not match what was expected.

You can customize the code further to return specific information to the user about what happened.

Using nonces in your code is a fast, easy, and effective way to prevent many types of hacking attempts. That does not mean you can skip doing all the other security measures, but it helps reduce the worst problems.

Remember what I said about never trusting anybody? That brings us to another way to protect your code – sanitizing.

## Grab a free copy of our Cheat Sheet for Selling Plugins and Themes

A growth roadmap with concise, actionable tips for every milestone of WordPress product development.

![blue book with the title “Cheat Sheet for Selling Themes and Plugins by Freemius” written on it](https://freemius.com/blog/wp-content/plugins/fsblog-utilities/assets/img/svg/cheat-sheet-ebook.svg)

## 5. Sanitize user input

In the previous example, we included an additional piece of data sent from JS to PHP. Every time you get data into your code you should expect it to be unsafe.

`'user_data':'Some input from a user'`

In this example, it is a simple string, but since we are sending data back to PHP we need to ensure that the input does not contain any code that could be exploited in our PHP environment or be stored in the database allowing for further abuse.

In comes sanitization. WordPress has a range of functions that takes whatever input you give it and cleans the data before returning it to you.

In this example, we used the function `sanitize_text_field()`, but [WordPress comes with many sanitizing functions](https://developer.wordpress.org/?s=sanitize_) suited for different types of data.

![TV reporter spraying 2 Lysol](https://freemius.com/blog/wp-content/uploads/2020/11/word-image-2.gif)

There are many other great functions and methods built into WordPress that you can use to keep your code secure and prevent abuse.

You should never, ever use any data sent to your code without sanitizing it first. Check out [this article about common WordPress developer mistakes](https://freemius.com/blog/5-common-mistakes-wordpress-plugin-developers-should-avoid/) with more details about sanitizing and other great practical tips.

And that brings me to the next tip, which most WordPress developers have experienced:

## 6. Remember that `is_admin()` is not what you think

When you first start thinking about protecting your code from evil, you will probably stumble across the function `is_admin()`, and from the name, it sounds to be everything you need, and all you need to do is wrap your code with that, and all will be well.

No, unfortunately not. The function `is_admin()` only detects if the code is being executed on the administration side of the website. It does nothing to detect if your code is being run by a regular user or administrator.

You will never notice it if you just enter the code in your plugin because you are most likely running the code in the administration interface, and that means the code will just evaluate to `true`, and you will stop thinking about it and move on to something else.

The correct way to check if a user is an administrator is to check the user capability:

```
  if ( current_user_can( 'activate_plugins' ) ) { 
    // Do your code here
  }
```

There are different capabilities for different user roles, so you have much more granular control. In most cases, `’activate_plugins’` is what you need for admins only.

If you want a way to allow [both administrators and editors to do something](https://wordpress.org/support/article/roles-and-capabilities/#administrator), you should test for the `’edit_pages’` capability.

## 7. Add rel=”noopener” or rel=”noreferrer” to your links

Linking to external resources is quite normal, and the old-school method of adding `target="_blank"` to those links makes sense because you do not want your users to leave your plugin/theme page.

However, this opens you up for what is called [Tabnabbing](https://en.wikipedia.org/wiki/Tabnabbing). This is a security problem where malicious JavaScript code can steal information from your users by abusing the JavaScript `window.opener` feature.

Preventing this can be as simple as adding `rel="noopener"` to your links. The page you link to today might be just fine, but that could change in the future.

**`rel=noopener`** means the page you link to cannot access information or gain any control of your page.

**`rel=noreferrer`** does the same, and also instructs the browser not to pass any referral information via the Referrer header. Adding `rel="noreferrer"` means the page you link to does not know where your visitor originates.

*Note: These two properties should not be confused with `rel=nofollow`, which is related to SEO.*

## 8. Use HTTPS and Secure Tokens with 3rd Party APIs

As a developer, you will often have to integrate APIs, and it is vital to do this securely to protect the data you are sending back and forth.

Fortunately, there are already standards set in place on how to do this safely; one of them is HTTPS. Using HTTPS introduces a layer of security where all the data transmitted is encrypted.

However, to ensure your data is protected from spying eyes, using HTTPS is not enough.

As [this article by Ars Technica explains](https://arstechnica.com/information-technology/2016/07/https-is-not-a-magic-bullet-for-web-security/), “HTTPS does not mean your data is secure, it just means your connection is secure.”

### Secure tokens – JWT

A secure standard to handle communication and API integrations is by using JSON Web Tokens, JWT.

A secure token is created by making a request to a server that validates a user’s login details and generates a token, a small piece of string that contains data, such as username, ID, and so on.

When you send any subsequent requests to the server, you include that token in the request. This token proves you are authenticated and have access. If the token is valid and it has not expired, the server will use the user details contained in the token and pull up the requested data.

The server can quickly process requests this way, in comparison to using an API key, which would require to look up the user via that key before deciding to process the data. Using a token, you can include data inside the token about the user and save multiple database queries.

With the way a secure token is generated and subsequently used, it is not possible to create fake tokens or manipulate the content of a token. It is only possible to create a valid token by knowing a secret key, which the company behind the platform will keep well hidden.

A very important note to remember is that data inside a token is not encrypted. It is impossible to tamper with the token contents without invalidating it, but the data inside a token can easily be read by anyone, so it is not a good place to store sensitive data.

A good resource if you want to dive more into tokens and how they work is the [Introduction to JSON Web Tokens](https://jwt.io/introduction/).

## 9. Do not use external libraries from CDNs

Although it can be tempting to include any libraries you might need via cdnjs.com or other free global CDNs, there are a few downfalls.

First of all, you have no control over the libraries and any malicious code that sneaks into the files you include.

Although CDN’s are generally stable and fast by definition, they are also subject to more attacks. If your code relies on a JS library on a CDN under attack, then your plugin and theme will load either very slowly or not at all.

This happened to a customer website where the public CDN a plugin was using at the time was timing out for users in some regions making the interface unusable. In the end, I had to change the plugin to use a local copy of the JS script instead as a quick fix.

Using an external 3rd party source could also compromise privacy. It will be possible for the CDN to log all your user IPs – make sure to check the GDPR policy and inform your customers.

In general, if you use reputable 3rd party CDN providers, you will not face any problems, but the simplest and most reliable approach is to distribute the JS library included in your product.

**Did you know?** WordPress comes with several JS libraries included. Many of the more common JS libraries that you might want to use comes included with WordPress. [These libraries](https://developer.wordpress.org/reference/functions/wp_enqueue_script/#default-scripts-and-js-libraries-included-and-registered-by-wordpress) will cover most of your basic needs.

*Developer tip: Please only load the extra JS and CSS files on the specific pages you need. As a developer and a user, I highly dislike plugins that slow down the admin by loading unneeded JS and CSS files on every page. It not only slows down other admin pages, but it can also really mess with the visual layout and make some admin pages almost unusable. Please 🙂*

There are also some tools out there that can help you protect your code, and a great tool that you can use for free is Coderisk.

## 10. Use tools and services to analyze your code

### Coderisk

There are many automated services to help identify code issues. [Exakat](https://www.exakat.io/), [SonarSource](https://www.sonarsource.com/php/), and [PHPStan](https://phpstan.org/) to name a few, and a favorite of mine – [Coderisk.com](http://coderisk.com/) – An easy way to find some of the more obvious security errors in your code.

This company scans all WordPress plugins from the public WordPress.org repository. Their software is able to scan and identify hundreds of different kinds of security issues based on different coding standards.

According to their own statistics, they’ve scanned over 4 billion lines of public code so far, and there are quite a lot of issues with even the top plugins.

To sign up for their free service is quite simple – you can create a free account and then start claiming your plugins. Claiming a plugin is as simple as taking a single line of code that you put in your readme.txt next time you deploy a new version.

This allows you to access their latest scan of your plugin, and inside, they have specific information and details about each issue, with links directly to your code.

**![Coderisk Security Dashboard](https://freemius.com/blog/wp-content/uploads/2020/11/coderisk-security-dashboard-2.png)**

Keep in mind, this is a free service, so they might not update their scan of your plugin that often, but once you get a notification, it is worth checking your code, as you might have introduced a mistake since the last time you reviewed your code.

The interface is pretty easy to navigate once you get the hang of it, and the system is very useful, giving you very easy to understand instructions about what is wrong that helps you trace the error.

There are also a lot of ways to filter through bugs, and you can mark each issue as fixed or a lot of other options to help you quickly get an overview of all the issues.

**Note:** If you never run Coderisk (or any other tool in its category) on your code, don’t get concerned about the number of suspected issues you’ll get warned about. These tools may generate a good amount of false-positives as they only analyze the code without understanding the business logic. Use the tool’s output as a solid starting list of items to review.

### PHP\_CodeSniffer

Another great tool for checking your code is [PHP\_CodeSniffer](https://github.com/squizlabs/PHP_CodeSniffer). The PHPCS consists of two scripts, PHPCS that checks your code and reports errors to you and the PHPCBF that can automatically fix a long range of the problems that PHPCS identifies.

Using PHPCS is very easy to use from the command line once you have it installed. This tool will not prevent security problems showing up in your code, but you can eliminate simple coding mistakes which makes it that much harder to abuse any bigger issues.

It is also possible to integrate PHPCS directly into your editor, such as Sublime Text and Visual Code. This way you can easily see any mistakes and fix them quickly in your IDE.

No matter if you work in a team or as a single developer, it is worth using an automated system as it is an easy way to eliminate basic security issues you might otherwise miss.

Using an automated system to scan your code for security issues is not a safe catch-all-bugs method, but it can help you pinpoint the most obvious mistakes.

## 11. Don’t copy-paste code from the web without a proper review

Keeping your WP product as secure as possible should be an ongoing process, not just once in a while. When you introduce new features or remove code you can also introduce new security issues.

Google is not always your friend. As a developer, you are used to checking the big wide internet for code examples to inspire you – or just rewrite bits and pieces here and there if you are lazy.

Most of the pieces of code you find on the internet are rarely ready for use in a secure production environment and are meant as an example of whatever coding problem you are trying to fix. Using these pieces of code blindly and without review can introduce problems very quickly.

There is a lot to do as a WordPress developer, and fixing an urgent security issue in your plugin with thousands of installations should not be one of them.

## Keep in mind that your reputation is at stake

If you’re not paying attention to your plugin or theme security, you’re putting your users, their businesses, your business, and your reputation at stake. That is a lot of potentially wasted time and money!

Security vulnerabilities can have a massive impact on the trust and confidence that customers put into your brand or products. The Loginizer example above goes to show that even the most embarrassing security vulnerabilities can happen to security plugin developers themselves! And the other examples about voter fraud and government hacks tell us that anyone is vulnerable.

If and when you discover a vulnerability, act quickly to resolve it, and follow best practices for announcing the issue publicly (if necessary) along with releasing a fix.

If you stay ahead of the game when it comes to communication and the “public relations” issues that might arise from a vulnerability, then you can avoid some giant headaches and increase your reputability instead of damaging it.

### Thanks for Reading!

It can be daunting to look into all the things you need to do when you do not know what to look for to begin with, and it can be hard to find the right information. If you do not have a clue where to begin you should consider getting your product reviewed by a WP security expert (I do security reviews too).

It is tempting to save the money or the time for a security review, but the cost of not securing your product as much as possible can be even higher in the long run.

These are just *some* of the ways you can and should protect your WordPress product from being abused. If you have any doubt, just remember – Don’t trust anybody 🙂