Serving others, identifying the right opportunity at the right time, and putting in good old-fashioned grit have been the key factors to success for Senol Sahin’s content generation plugin AI Power.

At the end of 2022, Senol submitted [AI Power](https://aipower.org/) to the WordPress.org repository and the rest is (brief 😅) history. His product is now widely regarded as one of the best ChatGPT-powered plugins on the market.

In this article, Senol shares his story and provides insights about what he thinks the AI product market will look like in the near future.

[![Showcase of AI Power Plugin's Features](https://freemius.com/blog/wp-content/uploads/2024/04/showcase-of-ai-power-plugins-features.png)](https://freemius.com/blog/wp-content/uploads/2024/04/showcase-of-ai-power-plugins-features.png)

## Hi Senol — thanks for joining us! Please tell us more about yourself.

Hi, thanks for having me. I’m Senol Sahin from Istanbul, Turkey. I’m passionate about creating genuinely beneficial things because I believe making a positive impact on others’ lives is how you find meaning.

This driving force has always been at the heart of my endeavors.

## A noble philosophy 🪄 This leads me to the next question: How did you identify a gap in the market for an AI content creation plugin?

The journey began while I was working on content generation with a client using OpenAI’s API services. We’d send requests to the API and generate content in Google Sheets.

The most advanced model was text-davinci-002, but it still had difficulty producing longer content. I often worked late into the night, trying to edit longer pieces of content together by sending multiple separate API calls and combining them. It was a demanding process 😓

When [text](https://bundleiq.medium.com/comparing-gpt-3s-davinci-text-002-to-davinci-text-003-302e3ba951d5)[-davinci-003](https://bundleiq.medium.com/comparing-gpt-3s-davinci-text-002-to-davinci-text-003-302e3ba951d5) rolled out in November 2022, it was a significant improvement in AI. Generating longer and better content became more feasible. I still consider it one of the most impressive models as it was launched before the era of juggernauts like GPT-3.5 or GPT-4 models.

The turning point for me was when my client requested that we integrate the Google Sheets content generation process directly with WordPress. I obliged but it sparked a crucial realization:

**Instead of generating content outside of WordPress and feeding it back in, why not do it inside to begin with?**

This gave me the idea for a WordPress plugin.

Despite having limited experience in WP plugin development, I knew what the software needed and how it had to operate, so I hired a freelance developer to create a basic boilerplate.

The layout was simple:

1. A form to enter the OpenAI API key
2. A text field for a title
3. A ‘generate content’ button

[![First Version of AI Power Plugin Settings Page in WordPress](https://freemius.com/blog/wp-content/uploads/2024/04/first-version-of-ai-power-plugin-settings-page-in-wordpress.png)](https://freemius.com/blog/wp-content/uploads/2024/04/first-version-of-ai-power-plugin-settings-page-in-wordpress.png)

The first version of the plugin settings page

I started work on the boilerplate, learning about WordPress filters, actions, and plugin development as I went.

Eventually, I got the form to interact with the OpenAI API, receive responses, and save them as drafts in WordPress. The moment I saw it all come together, I was overjoyed. I [submitted the plugin to the WP.org repository](blog-submit-plugin-wordpress-repository.md) and went through a few rounds of revisions to meet their guidelines.

> A remarkable thing happened. One morning, I woke up to find that not only had my plugin been approved, but it had already been downloaded hundreds of times!

This immediate surge in downloads occurred without any marketing on my part, which I believe was due to its unique position as the first AI-related plugin in the repo. As downloads increased day by day, so did user requests and feedback. This marked the beginning of an exciting journey, and the plugin has continued to grow since then.

## Proof that hard work pays off! AI Power is [regarded as one of the best ChatGPT-powered plugins on the market](https://aipower.org/). Where do you see the future of WordPress and AI going?

WordPress is a great ecosystem for product development. The more I delve into it, the more I appreciate its capabilities. It’s fundamentally a platform for content, and AI is a valuable tool for content creation.

**This synergy opens up tremendous opportunities.**

Looking ahead, I see AI playing a more integral role in personalizing user experiences on WordPress sites, automating content curation, and even aiding in SEO. The potential for AI-powered analytics to provide insights into user behavior and content efficiency is also immense.

> In terms of product opportunities, I envision a future where AI plugins will offer smart content management by suggesting optimizations, tracking performance, and dynamically adapting content based on audience engagement.

Furthermore, AI could enable more sophisticated language translation capabilities, making WordPress sites more globally accessible and inclusive.

## Subscribe and grab a free copy to start Mastering SEO on the WordPress.org Repository

Make the WordPress.org search algorithm work for you with actionable tips to rank your plugin higher.

![Mastering SEO on the WordPress.org Repository](https://freemius.com/blog/wp-content/plugins/fsblog-utilities/assets/img/svg/cheat-sheet-ebook.svg)

## Returning to the present: What are the biggest challenges of running an AI-based plugin in WordPress?

The most significant one is the reliance on third-party AI services like OpenAI, Azure, and Google. Since the plugin’s functionality is dependent on these services, any issues or downtime on their end can mistakenly give users the impression that the plugin is malfunctioning.

To mitigate this, I’m continuously working to integrate more AI service options. This way, if one service experiences issues, users can still use the plugin effectively with the other available services.

## And in terms of business, what’s it like to do this by yourself? Do you have plans to branch out and onboard team members?

I’m handling the development and management solo and, honestly, I’m thoroughly enjoying it.

> The feedback and feature suggestions I receive from my supportive user community are invaluable. In fact, most of the features in the plugin were pitched to me by them.

I don’t have plans to expand the team, but it’s a possibility I might consider in the future. Interestingly, before the release of the GPT-3.5 model, I occasionally sought help from other developers on freelance sites. But since GPT-3.5’s release, I’ve been using AI to write code and fix bugs, which has been an efficient, fascinating process.

[![Senol Sahin's Task List of Code to Write and Bugs to Fix Using AI](https://freemius.com/blog/wp-content/uploads/2024/04/senol-sahins-task-list-of-code-to-write-and-bugs-to-fix-using-ai.png)](https://freemius.com/blog/wp-content/uploads/2024/04/senol-sahins-task-list-of-code-to-write-and-bugs-to-fix-using-ai.png)

## AI Power can cater to a huge market — not only WordPress. I recently wrote a three-part series about [converting your WordPress plugin to SaaS](blog-how-to-convert-plugins-to-saas.md). Is this something you’ve considered?

Right now, I’m not considering moving to a SaaS model. My primary focus is to continue developing and enhancing the plugin within the WordPress ecosystem.

> Sticking to the WordPress platform allows me to dedicate my efforts to refining and evolving the plugin to best serve the needs of the WordPress community.

## Fair point. I see AI Power has 10,000 active installs on WP.org. What do you believe has contributed most to its success and what features set you apart from competitors?

The success of the plugin comes down to being **first in the market, understanding user needs, and executing well**.

It stands out because it’s not just focused on content generation or chatbots. It’s a complete AI package that offers a holistic solution covering a wide array of functionalities that go beyond what typical AI plugins offer. Such as:

- Vector database integrations
- Image generation from various AI providers
- AI training tools
- Fine-tuning capabilities

## Have you had any lucky breaks that contributed to your success?

Some luck played a role in my journey, particularly in quickly recognizing the need for an AI plugin in the WordPress ecosystem.

My prompt action and fast execution were key. Had I spent too much time planning or organizing sprints, the outcome might have been different. Starting with just a simple form and releasing it allowed me to adapt and expand based on real user feedback and needs, which has been fundamental to the success of the plugin.

## What about challenges and obstacles?

The most significant challenge I faced was not being a developer myself. While I had clear ideas and understood what was needed, I lacked the coding skills to bring these ideas to life. This meant I had to find competent developers and effectively communicate my vision to them.

Fortunately, with the advent of GPT-4, I’ve been able to use its capabilities to write the code, significantly easing the process and helping me overcome this hurdle.

For example, I’m currently integrating [Qdrant](https://qdrant.tech/) (vector db) into my plugin as an alternative to Pinecone and — impressively — all the code for this integration has been written by GPT-4. In the past, this required hiring a developer, explaining the task, and then waiting for completion.

[![First Image of ChatGPT Writing the Code for Qdrant Integration](https://freemius.com/blog/wp-content/uploads/2024/04/first-image-of-chatgpt-writing-the-code-for-qdrant-integration.png)](https://freemius.com/blog/wp-content/uploads/2024/04/first-image-of-chatgpt-writing-the-code-for-qdrant-integration.png)

[![Second Image of ChatGPT Writing the Code for Qdrant Integration](https://freemius.com/blog/wp-content/uploads/2024/04/second-image-of-chatgpt-writing-the-code-for-qdrant-integration.png)](https://freemius.com/blog/wp-content/uploads/2024/04/second-image-of-chatgpt-writing-the-code-for-qdrant-integration.png)

ChatGPT writing the code for the Qdrant integration

## You probably don’t want to spill all the beans but are there any tips for success you can recommend to aspiring AI product creators?

> My key advice to AI product creators is to diversify the AI providers integrated into their products.

Rather than relying solely on one provider like OpenAI, it’s good to include options from Google, Microsoft, Claude, Mistral, Llama, etc. This approach not only offers flexibility but also ensures reliability and a wider range of capabilities for users.

## Please tell me more about your dev environment. Don’t hesitate to geek out!

Sure:

- I’m currently working on a 2022 model MacBook Pro M2, which has been fantastic for my needs.
- For coding, I primarily use Visual Studio Code.
- When it comes to documentation, I use Docusaurus to create my documentation website, making sure to update it consistently with every new feature, no matter how small.
- Since WordPress is PHP-based, my coding mostly involves PHP and JavaScript.
- I use GPT-4 for all my coding tasks, which has been a game-changer for my development process.

## What tools and devices are essential for your business?

GPT-4.

It’s become an indispensable part of my workflow. I’ve uploaded my entire codebase to it and have fine-tuned it according to my specific needs. This enables it to fix bugs and add new features to the app efficiently.

> The level of integration and assistance GPT-4 provides is so significant that I can’t imagine going back to the traditional way of hiring developers for these tasks.

[![The Latest Design of the Knowledge Builder Module that was Created by GPT-4](https://freemius.com/blog/wp-content/uploads/2024/04/the-latest-design-of-the-knowledge-builder-module-that-was-created-by-gpt-4.png)](https://freemius.com/blog/wp-content/uploads/2024/04/the-latest-design-of-the-knowledge-builder-module-that-was-created-by-gpt-4.png)

The latest design of the knowledge builder module that was created by GPT-4

## Amazing — it seems like the concept of ‘no-code’ is taking on a different meaning. Moving on, I’m interested to know what influenced your decision to opt for Freemius.

Upon release, I didn’t intend to monetize AI Power — I was more curious to see if it would work 😅 As the downloads increased and user feedback started pouring in, I realized there was a demand for it.

Despite this, the plugin remained free until a conversation with a user on Discord changed my perspective. The user expressed a willingness to [pay for an additional feature](blog-paid-customization-plugins-themes.md): adding a keyword option for the content writer module. That was the moment I started to consider monetization.

I researched ways to [monetize a WordPress plugin](blog-how-wordpress-plugin-developers-make-money.md). In Turkey (where I’m based), many online payment systems like PayPal are banned, which limits my options.

During my search, I stumbled upon Freemius. I hadn’t heard of it before, so I looked for alternatives to compare. After thorough research, I concluded that Freemius was exactly what I needed.

**The more I used it, the more impressed I became.**

> Freemius offers everything a developer requires to monetize a product, from email management and payment processing to handling refunds. It’s been an excellent choice for my needs.

## Flattering words 😊 Let’s unpack the features that impress you.

There are several standout Freemius features that I find particularly appealing:

1. [**Easy Integration**](help-documentation-getting-started.md#integration_deployment_process): Integrating Freemius with my plugin was surprisingly straightforward. It was just a matter of adding a piece of code, and that was it. I was truly astonished by the simplicity.
2. [**Recurring Payments and Subscriptions**](wordpress-recurring-payments-subscriptions.md): This feature enables a steady, predictable revenue stream, which is crucial for my long-term planning and my business’s sustainability.
3. [**Selling from the WP Admin Dashboard**](help-documentation-selling-with-freemius-so-what-does-freemius-do.md): I consider this a game-changer. It simplifies the process for users, making it more integrated and seamless.
4. [**User Dashboard**](wordpress-user-dashboard.md): The dashboard is comprehensive, offering everything a user needs. It’s user-friendly and adds significant value to the overall user experience.
5. [**Dunning Mechanism**](https://freemius.com/help/documentation/selling-with-freemius/dunning-failed-payments/): This works exceptionally well in managing failed payments, which is vital for maintaining consistent revenue.
6. [**Email Management**](help-documentation-marketing-automation-transactional-emails.md): The ability to send automated emails to users based on their payment actions and other triggers is highly beneficial for maintaining good customer relationships.

## How has Freemius contributed to the growth of AI Power?

Freemius has been instrumental in its growth by enabling monetization, primarily.

The financial growth has directly contributed to the continuous development and expansion of the plugin, allowing for the addition of more features and enhancements. Essentially, Freemius has provided the means to transform AI Power from a free tool into a sustainable, evolving product.

## Following on, how has Freemius influenced your revenue?

Freemius has had a 100% influence on my revenue. Before integrating with the platform, my plugin didn’t generate anything. Freemius provided the necessary tools and framework to monetize, marking the start of my revenue generation.

## Following the implementation of Freemius, have you observed any other noteworthy results or success metrics?

Yes. One particularly surprising result was the detailed user statistics provided by Freemius.

The [Audience Analytics Dashboard](blog-release-notes-real-time-analytics-and-multi-store-dashboard.md) offers insights into the geographical distribution of my users, showing me which countries they are from. This was information I never had access to before, and it’s been enlightening to see the global reach of my plugin.

[![Freemius Audience Analytics Dashboard](https://freemius.com/blog/wp-content/uploads/2024/04/freemius-audience-analytics-dashboard.png)](https://freemius.com/blog/wp-content/uploads/2024/04/freemius-audience-analytics-dashboard.png)

## If you’ve contacted our support team, tell us about the experience.

I’m impressed with the support I’ve received from Freemius.

> The experience of getting direct responses from lead developers like Leo has been fantastic. The team has consistently responded within 24 hours and resolved my issues on the same day, which is exceptional.

## I’m really glad to hear that! Okay, so hear me out. By some twist of fate, you get to redo the first year of launching AI Power. What would you do differently, and what wouldn’t you change?

If I had that chance, my approach would be to keep things simpler. One aspect I wouldn’t change, though, is my ***just execute, don’t overthink or overplan*** mentality.

## How do you think AI will shape the future of your (AI) business?

I no longer need to hire developers for certain tasks because I use GPT-4 to write code. This kind of AI integration is revolutionizing how work is done, indicating that a scenario of AI handling most of the workload while I relax on a tropical island isn’t as far-fetched or science fiction-y as it once seemed.

The pace of AI development suggests that this reality might be closer than we think.

## Thanks for your time, Senol, and we wish you well in the future! Before you go, please drop your social handles so that people know where to find you.

Thank you for having me, it’s been a pleasure!

For those interested in connecting and staying updated, we have a vibrant Discord community.

You can join us [here](https://discord.gg/UJ3fqMx6su).

Looking forward to interacting with more people passionate about AI and WordPress!