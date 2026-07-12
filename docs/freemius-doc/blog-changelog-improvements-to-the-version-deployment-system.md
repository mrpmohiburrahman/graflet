[Changelog](https://freemius.com/changelog/) / Improvements to the Version Deployment system

Our [Version Deployment](https://freemius.com/help/documentation/selling-with-freemius/deployment/) feature is a powerful tool for developers. Recently, it came to our attention that the [readme.txt](https://freemius.com/help/documentation/selling-with-freemius/deployment/#handling_premium_readme_txt) processor was unintentionally adding extra line spaces while stripping codes in between `[//]: # fs_{free|premium}_only_{begin|end}` tags.

[![Improved readme.txt parser in Freemius Version Deployment system](https://freemius.com/blog/wp-content/uploads/2024/03/improved-readme-parser-freemius-1024x673.png)](https://freemius.com/blog/wp-content/uploads/2024/03/improved-readme-parser-freemius.png)

We’ve fixed the issue and added improvements to handle both block and inline tags. As seen above, texts are properly stripped off and consistently maintain the space and new lines.