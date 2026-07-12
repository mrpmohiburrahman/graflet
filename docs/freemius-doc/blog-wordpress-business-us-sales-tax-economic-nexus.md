US sales tax is an ever-growing thorn in the side of solopreneurs and SMBs 🌵 As of 2018, anyone selling software and SaaS products in the US must collect US sales tax from customers based on where they reside, regardless of the seller’s physical location. What does this mean for US-based WordPress and SaaS developers? Should you be looking to safeguard yourself and your business?

To unpack the matter, we’ll examine:

- How and why US sales tax came about
- What economic nexus is
- How US sales tax works
- Why US sales tax is especially painful for US-based WordPress and SaaS businesses
- How to be US sales tax compliant

## Understanding US Sales Tax: What Is It and How Did It Come About?

Let’s backtrack to see how and why the United States got to the point of imposing sales tax.

### South Dakota v. Wayfair

A 2018 Supreme Court case known as *South Dakota v. Wayfair* ruled that US states should be entitled to collect taxes from vendors that do not have a physical presence in a state but conduct business within it. This changed the long-standing physical presence (aka nexus) rule from the 1992 *Quill Corp. v. North Dakota* case which dictated that — in a nutshell — businesses were only required to pay taxes to states where they had physical presence (like offices or warehouses).

The 2018 court case ruled that the internet has significantly altered the traditional business landscape and given an unfair advantage to eCommerce giants like Wayfair. Prior to 2018, they could manage their warehouses in sales tax-free states, which essentially allowed them to lower prices by cutting off sales tax.

As an example: before 2018, buying a $999 iPhone in an Apple Store in NYC would cost $80 more than buying it on Amazon.

Naturally, this negatively impacts solopreneurs and SMEs. As per [this article](https://www.cpajournal.com/2021/04/26/the-impact-of-the-u-s-supreme-courts-decision-in-south-dakota-v-wayfair/) by The CPA Journal:

*It is clear that the ruling puts small, developing businesses at a comparative financial disadvantage, and may in fact provide a death blow to some businesses given the cost of compliance.*

### Understanding Economic Nexus

As of late, there has been much talk about economic nexus and how it impacts online sellers. But what is it exactly?

In US financial terms, ***nexus*** denotes where your business has a physical presence(s) such as headquarters, employees, etc. For example, if you have full-time employees in three different states, you have three nexuses.

***Economic nexus***, on the other hand, is a newer term and a direct result of the *South Dakota v. Wayfair* ruling. Unlike the regular nexus, it defines where you have an economic presence sufficient to be considered a nexus. When you have a nexus in a jurisdiction — physical or economic — you need to start collecting and dealing with sales tax.

US sales tax and economic nexus didn’t appear out of the blue. Instead, the motivation to enforce them may also have been influenced by international developments.

### Inspired by the European Union VAT Laws? 🤔

The United States’ new position on imposing both individual state- and jurisdiction-based sales tax has likely been influenced by the principles that guide [European (EU) VAT](https://freemius.com/wordpress/collecting-eu-vat-europe/).

In the past, a European business would only collect VAT from consumers in the country they were based in and pay VAT rates according to that country. However, when the 1994 EEA agreement united the EU Member States and the three EEA EFTA States (Iceland, Liechtenstein, and Norway) into a single market and eCommerce simultaneously grew, governments realized they could raise more money by imposing VAT rates on foreign sellers, which officially commenced in 2015. Thus, the concept changed to charging VAT based on the customer’s geolocation instead of the country where a business is based.

Soon, other (non-EU) countries cottoned on to the perks of imposing GST on sellers outside their country.

Now that we have a solid understanding of how/why US sales tax came about, let’s look at how it works in principle.

## How Does US Sales Tax Work?

There are fifty US states, and each has its own sales tax laws and regulations. Adding to the complexity, every US state has jurisdictions (there are more than 11,000 of them in total), and every jurisdiction has its own \[read: **additional**] tax rates and regulations. These are also known as local sales taxes.

The combination of state-based sales tax and local sales tax sets the current average sales tax rate in the US between 0% and 9.55%. You can find out more about these stats in [this report by World Population Review](https://worldpopulationreview.com/state-rankings/sales-tax-by-state).

![Tax Foundation’s 2022 heatmap of sales tax rates in different US states](https://freemius.com/blog/wp-content/uploads/2023/08/word-image-1.png)

Tax Foundation’s 2022 heatmap of sales tax rates in different US states

Needless to say, the relatively new US sales tax/economic nexus has birthed a near-overnight spate of financial, legal, and administrative headaches for US-based WordPress and SaaS developers.

## The Pain Points of US Sales Tax for Developers

Let’s suppose a US-based WordPress or SaaS developer has been conducting business as usual since the *economic nexus* ruling ***without*** handling US sales tax.

Freemius has spoken to many developers who weren’t even aware that they needed to deal with sales tax collection in the USA. On the flip side, we met with developers who know about US sales tax but haven’t collected because they feel their business is too small to raise eyebrows and that state authorities aren’t purposefully out to prosecute them.

There is a rationale to this reasoning, but it’s unnecessary to make your business vulnerable to exposure if you don’t have to. Yes — paying taxes is a burden, but fear of exposure is debilitating.

The problem with US sales tax is that failure to comply is likely to cause far more problems for US-based WordPress and SaaS developers than EU VAT. As a US-based seller, if you fail to collect and report sales taxes from customers in — say — a European country, it’s less likely anyone will come after you. The country in question might impose a fine on you or deport you for owing them money if you ever land on their shores. But when it comes to US states, it’s quite easy for them to go after US sellers.

![US sales tax and economic nexus can cause huge headaches for WordPress solopreneurs and SMBs](https://freemius.com/blog/wp-content/uploads/2023/08/word-image-5.gif)

The reason states can readily prosecute US sales tax dodgers is because the US has official authority over US businesses. We are already seeing plenty of cases where US-based WordPress and SaaS businesses turning $30k to $80k a month haven’t collected US sales tax. They now face big exposure fines, and it’s extremely stressful for them.

Let’s run a rough napkin calculation of a US-based plugin business grossing $50k per month for 5 years, where 70% of its customers are from the US. That’s $2.1M in sales in the US alone.

For an average software business selling in the US, about 25% of sales are taxable. That’s $525k for which taxes were not paid. With an average 6% sales tax rate for downloadable software, the business has an exposure of $31.5k. The penalty is 10% of the tax due for the first month, plus 1% for each additional month or part of a month not exceeding 30%. That gets you to $41k of taxes that would need to be paid out of pocket.

Now, if you think about scaling the business to $100k per month, that’s already $82k in exposure. And over time, the exposure just grows with your business.

And the issue gets uniquely complicated for developers.

## How Can SaaS and WordPress Developers Comply With US Sales Tax?

Needless to say, calculating sales tax rates for every individual transaction based on the customer’s jurisdiction and state demands admin of epic proportions.

Here’s what you need to do to be compliant:

1. You need to identify the jurisdiction of every sale, which at minimum would require asking the buyer for their zip code.
2. Then, you need to have a mapping structure between zip codes and states in place.
3. For every state, you need to run a search to understand:
   
   - Whether the state collects sales tax
   - What the economic nexus thresholds are
   - Whether the product you’re selling is taxable and what the tax rate is (which also varies between B2B and B2C sales)
4. To save you the sweat and money on CPAs, we’ve provided access to Freemius’s complete and exclusive US sales tax research, specifically for downloaded software (plugins, themes, templates, and widgets) and SaaS:

### US Sales Tax Rates and Economic Nexus Research for Downloadable Software

** In some jurisdictions, tax rates apply only to a portion of the transaction for some products*

### US Sales Tax Rates and Economic Nexus Research for SaaS

** In some jurisdictions, tax rates apply only to a portion of the transaction for some products*

***\*\*Disclaimer:** As this writer is not an accountant, there may be typos in the above tables. If you spot anything, please let us know.*

Moving on…

- 5. For the states that impose an economic nexus where your products are taxable, you need to monitor your transactions count and sales volume. If you’ve reached the economic nexus threshold in the previous 12 months, current calendar year, or previous calendar year (it differs by state 🤯), you’ll need to register in the state for sales tax.
  6. After registering, you’ll need to start collecting sales taxes for the registered states. Oh, and let’s not forget our beloved active subscription renewals 🙂 You’ll need to analyze your subscriptions database and update all relevant subscriptions so that next time a renewal is processed in a jurisdiction where you recently registered, the sales tax amount will be added to the renewal. You’ll also have to inform affected customers of the additional sales tax in advance so as not to smear business relations.
  7. In parallel, you’ll need to monitor state tax changes, both on the tax rates as well as other updates. For example, a state can change its economic nexus threshold, decide to start taxing software, or implement additional measures that you personally wouldn’t want to deal with and should probably get an accountant or a sales tax person to handle. And every time such a change arises, you’ll need to update your system and assess the impact on subscriptions.

## Subscribe and grab a free copy of our WordPress Plugin Business Book

Exactly how to create a prosperous WordPress plugin business in the subscription economy.

![The WordPress Plugin Business Book](https://freemius.com/blog/wp-content/plugins/fsblog-utilities/assets/img/svg/cheat-sheet-ebook.svg)

## Isn’t That Crazy?!

I’m sure that at this point you’re rightfully asking yourself, *Do I really need to deal with all of this 💩 myself as an indie-developer or small company to be compliant? Isn’t there a solution to handle all of this for me?*

There are **MEGA** companies like Avalara and TaxJar that specialize in taxes. An alternative route would be to use their services and integrate with their APIs to save you some of the heavy lifting.

The problem with this route is that when you start dealing with these giants, you soon realize their pricing isn’t viable for typical SaaS or WordPress product businesses. Instead, it’s aimed towards enterprises because it’s priced per transaction. You’ll end up paying tens of thousands of dollars per year for US tax compliance alone. This is something that everyday product makers can’t afford. And — frankly — it’s unfair that they should be concerned over these matters in the first place.

Considering the implications of avoiding US sales tax and the complexities of committing to remain above board, what is a dev to do?

## There’s Another Way: It’s Called a Merchant of Record Solution (MoR)

An MoR is a legal entity that takes care of all billing-related responsibilities like subscriptions and invoicing and is liable for every payment made by buyers purchasing software products or SaaS. It keeps track of and compiles all due sales tax payments, ensures PCI compliance, and handles any fraud, refunds, and chargebacks.

## How Freemius Helps WordPress and SaaS Developers With US Sales Tax

If you’ve got a backlog of undeclared sales taxes, it’s in your best interest to contact an accountant to help you get your affairs in order. And if you’d like to keep your house squeaky clean going forward, a managed platform like Freemius can take care of your US sales tax affairs so you can focus your time and energy on developing awesome software products.

We work with US tax experts to determine the correct product categorization in each state, the required tax rate, updating subscriptions, monitoring sales tax rate changes, and everything else required to comply.

Why would we want to deal with this mess?

As a Merchant of Record, we are liable for sales tax compliance (and many other regulations like EU VAT, GDPR, LGDP). In fact, if we get things wrong, this liability is our problem and you simply don’t need to worry about it.

If you have additional questions on US sales tax or would like to sign up for our services, please get in touch with us at [\[email protected\]](https://freemius.com/cdn-cgi/l/email-protection#cba8a4a5bfaaa8bf8badb9aeaea6a2beb8e5a8a4a6).