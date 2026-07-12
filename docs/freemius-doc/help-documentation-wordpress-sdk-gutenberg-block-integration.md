---
title: "Gutenberg Block Integration"
url: "https://freemius.com/help/documentation/wordpress-sdk/gutenberg-block-integration/"
source: "docs"
section: "Docs"
category: "WordPress SDK"
scraped_at: "2026-04-09T19:58:44+06:00"
word_count: 2960
---

Developing blocks for the Gutenberg editor is quite [straightforward](https://developer.wordpress.org/block-editor/tutorials/create-block/) these days as the project continues to mature; and there are numerous [tutorials](https://www.google.com/search?q=gutenberg%20block%20development&oq=gutenberg%20block%20development&aqs=chrome..69i57j69i60l3j0l2j0i22i30l2.5615j1j7&sourceid=chrome&ie=UTF-8) available to help create almost any type of block you want.

However, knowing how to *monetize* a block is not so immediately obvious and requires some approaches that you may not be familiar with. Using the techniques outlined in this guide will help you to overcome any potential issues, you might come across, during the integration process.

note

Note: It's assumed that you're already familiar with developing blocks for the Gutenberg editor. If not then we highly recommended working through the official [Gutenberg handbook](https://developer.wordpress.org/block-editor/) before attempting integration with the Freemius platform.

## Integrating a Block with Freemius[​](#integrating-a-block-with-freemius "Direct link to Integrating a Block with Freemius")

There isn't just one single method available when developing Gutenberg blocks, and each one requires a different approach to complete Freemius integration successfully. We'll look at the common types of block in this section and how you can make them work properly with Freemius.

For **paid only** blocks, integration is quite simple as there's no free version at all. Which means there aren't any features that need removing during deployment. This type of block can be structured pretty much as you wish as long as the code to load premium scripts etc., are wrapped with the usual Freemius [licensing logic](help-documentation-wordpress-sdk-software-licensing.md).

For **freemium** blocks, integration is usually more complicated as the paid features need separating out from the free code. If you've chosen to render block content via PHP then integration is also much easier as paid features can be wrapped with the same logic you're already used to.

e.g.

```php
if( fs()->can_use_premium_code__premium_only() ) {
  // paid logic here
}
```

Any paid block features written solely in JavaScript should be implemented via (JavaScript) [hooks](https://developer.wordpress.org/block-editor/packages/packages-hooks/) (see next section) so that they can be removed from the free plugin during [deployment to Freemius](help-documentation-release-management-deployment.md).

To help understand how to effectively add paid features to a block written in JavaScript only, we've added a [new Gutenberg-integrated plugin](https://github.com/Freemius/hello-dolly/tree/master/freemium%20v.3/hello-dolly) to our [Hello Dolly Freemium](https://github.com/Freemius/hello-dolly) repository that contains a fully working block, which monetizes certain features.

Specifically, the free features included in the plugin are:

1. One song ('**Hello Dolly**') available.
2. Refresh the displayed lyric for the current song via block inspector controls.

And the **paid** features are:

1. Choose to display lyrics from three extra songs, depending on the current active plan ('**Summertime**', '**Wonderful World**', or '**Dream a Little Dream**').
2. Optionally show the line number of the current song lyric (available in any paid plan).

We'll use snippets of code from [this block plugin](https://github.com/Freemius/hello-dolly/tree/master/freemium%20v.3/hello-dolly) throughout this guide to demonstrate the most relevant techniques you can use when monetizing your own blocks.

## The Need for JavaScript Hooks[​](#the-need-for-javascript-hooks "Direct link to The Need for JavaScript Hooks")

When you need to extend a block feature written in JavaScript then hooks are extremely useful and allow you to seamlessly add paid features.

They're available in WordPress core so just import them into your block code just like any other package:

```javascript
const { applyFilters, doAction } = wp.hooks;
```

Usage is similar to PHP hooks, where you pass in a default value to a hook:

```javascript
let some_option = applyFilters('some-option', [{ label: 'Some Option' }]);
```

Then the default filter value can be modified elsewhere in the codebase:

```javascript
const { addFilter } = wp.hooks;

addFilter('some-option', 'my-plugin/some-option', function (options) {
  // Add another options object to the array.
  options.push({ label: 'Another Option' });

  return options;
});
```

Normally, all block code (for one or more blocks) is compiled into a single file containing vanilla JavaScript. But when using hooks to implement paid features this isn't really useful as we need the paid features compiled to a *separate* file so it can be conditionally enqueued, and removed from the free version completely during deployment.

All you need to do is make sure your build process is set up to produce *separate* files for free and paid features.

In the Hello Dolly plugin the [@wordpress/scripts](https://developer.wordpress.org/block-editor/packages/packages-scripts/) package is used to compile the JavaScript code. To make sure code is compiled to separate files a couple of new scripts were added to `[package.json](https://github.com/Freemius/hello-dolly/blob/master/freemium%20v.3/hello-dolly/package.json)` for development and production builds:

```javascript
"build:custom": "wp-scripts build src/blocks/song-lyrics/index.js src/pro/extend-blocks.js",
"start:custom": "wp-scripts start src/blocks/song-lyrics/index.js src/pro/extend-blocks.js",
```

## Localizing Freemius Data[​](#localizing-freemius-data "Direct link to Localizing Freemius Data")

To enable/disable paid block features we need to access Freemius license, and plan data, via JavaScript.

This isn't directly possible at the moment, but in the future, we plan to provide a richer JavaScript SDK which will handle license-related logic in a similar manner to how our PHP SDK does it.

In the meantime though, we can [localize](https://developer.wordpress.org/reference/functions/wp_localize_script/) Freemius data and manually pass it to JavaScript via PHP.

Data can be localized as follows:

```php
$licensing = array( 'can_use_premium_code' => my_fs()->can_use_premium_code() );
wp_localize_script('my-script', 'my_block_licensing_data', $licensing);
```

Add whatever data to the PHP array that you need to access via JavaScript. This localized data can then be used directly in your block code (as it's automatically available via a global JavaScript object).

```javascript
const licensing = my_block_licensing_data ? my_block_licensing_data : null;

if (licensing.can_use_premium_code) {
  // ... premium only logic ...
}
```

The major benefit of this method is that you can fully test paid features locally **before** deploying. Switching licenses that have different active plans will enable that functionality automatically. Or, deactivating the license will just revert the block to free features only.

Being able to test block features locally like this can really speed up development time!

## Monetizing JavaScript Rendered Blocks[​](#monetizing-javascript-rendered-blocks "Direct link to Monetizing JavaScript Rendered Blocks")

Blocks written purely in JavaScript need extra considerations compared to PHP blocks. Any JavaScript feature can be monetized but the key is *how* it's implemented. Some features are easier to monetize than others because of the way JavaScript blocks are rendered.

If your block implements extra features via changes to the [`edit()`](https://developer.wordpress.org/block-editor/developers/block-api/block-edit-save/#edit) function then you won't have any issues. You can go ahead and use JavaScript hooks to separate out paid features as shown in the previous section.

But if you're adding paid features that update the blocks [`save()`](https://developer.wordpress.org/block-editor/developers/block-api/block-edit-save/#save) function directly as soon as the license is activated, then (when the block is loaded inside the post editor) you'll almost certainly see a block invalid content warning.

This dialog box does actually allow you to update the block to the new version that includes paid features just by clicking the **Attempt Block Recovery** button.

However, the UX is still pretty unfriendly. You wouldn't really want to show this to a user when updating block content directly as it looks like some unidentified error has occurred.

There are plans to [address](https://github.com/WordPress/gutenberg/issues/25436) this issue and improve the UX but the proposal has no definite time-frame for implementation. So, until then it's probably best to avoid triggering the block invalid content warning wherever possible.

### Managing Direct Changes to Block Markup[​](#managing-direct-changes-to-block-markup "Direct link to Managing Direct Changes to Block Markup")

Fortunately there are other methods you can use to avoid the block invalidation warning.

For very small changes to the save content, that are enabled in paid plans, you can simply include the markup in the free version and disable UI controls to access/update them.

In the Hello Dolly Freemium plugin this method is used to show the line number of the lyric for the currently selected song:

```javascript
const { applyFilters, doAction, createHooks } = wp.hooks;
const { Fragment } = wp.element;

export function Markup(props) {
  const { song, lyric, lineNumber, showLineNumber } = props;

  return (
    <Fragment>
      <span style={{ fontWeight: 'bold' }}>{song}</span>: {lyric}{' '}
      {showLineNumber && (
        <span style={{ fontStyle: 'italic' }}>({lineNumber})</span>
      )}
    </Fragment>
  );
}
```

The `showLineNumber` attribute is set to `false` initially so that it doesn't display until you upgrade to a paid plan and enable it. And if the license is downgraded to the free version or is deactivated then `showLineNumber` is reset to `false`.

The inspector controls to modify `showLineNumber` status are only shown in the paid version and these are actively stripped out from the free version (see next section). It's important to stress that only the bare minimum content is included with the free version and there is no easy way it can be accidentally enabled.

This approach is fine for **very small** changes to the save function, but is not recommended for substantial changes. If you wish to directly modify the rendered save content significantly (e.g. for license status changes) then you'll need to use another method.

One way to do this is to use the blocks `componentDidMount()` lifecycle method (or React hook equivalent).

If Freemius license/plan data is localized then you could store the current license status and active plan in block attributes and use it to compare against the passed in data every time the editor (re)loads. Then, if the license status (or paid plan) has changed then you could then trigger a block update via `componentDidMount()`.

This would **bypass the block invalid content warning** and update the block content automatically to the new version. The only caveat with this method is that a manual post update is required to persist changes (as new block changes have been detected). If you leave the editor without saving changes then the block will be auto-updated the next time it's viewed in the editor.

To summarise here are the main choices you have to manage block rendering when the blocks save content has been directly modified:

2. For **very small** markup changes include the bare minimum markup in the blocks save function needed for the paid feature and set the relevant block attribute(s) to `false`. Strip out inspector controls from the free version via JavaScript hooks, and don't forget to manually remove the block source code before deploying to Freemius.
3. Modify the blocks save content via the `componentDidMount()` lifecycle method (or React hook equivalent). A manual post update is required to persist changes.
4. Use PHP to render the save function content. This is about as bullet-proof as you can get and is an ideal solution if you also need to provide a shortcode as well as a block (e.g. to support 3rd party page-builders). However, there are many benefits to coding your blocks in JavaScript with the most obvious being that block changes update in the editor in real-time opposed to a small delay when using PHP as it needs to render on the server.
5. Do nothing! Allow the block invalid content warning message to be displayed when the block's save content is directly updated and leave it to users to update (a manual post update is required with this method too). Until the UX is improved then it's not really recommended that you use this method as you'll probably see a spike in support requests (e.g. reporting the block content is broken etc.)!

### Managing Non-direct Changes to Block Markup[​](#managing-non-direct-changes-to-block-markup "Direct link to Managing Non-direct Changes to Block Markup")

Blocks can also be monetized by adding options and controls to the block toolbar, or inspector panel. This involves making changes to the blocks `edit` function via JavaScript hooks. And because altering the `edit` function won't **ever** trigger the block invalid content warning this makes it a completely safe way to add paid block features!

In the [Hello Dolly Freemium](https://github.com/Freemius/hello-dolly/tree/master/freemium%20v.3/hello-dolly) block we've added three new songs that become available (depending on the current active plan) as soon as the license is activated. And whenever the license is deactivated the songs are no longer available.

To do this a filter was added for the songs available in the block inspector:

\[RadioControl.js]

```javascript
let song_options = applyFilters('song-list', [
  { label: 'Hello Dolly', value: 'Hello Dolly' },
]);
```

We can then use the filter to extend the list of songs available:

\[extend-blocks.js]

```javascript
addFilter('song-list', 'hello-dolly/song-lyrics', function (songs) {
  if (!hello_dolly_editor_data) {
    return 'Error, Freemius data not found!';
  }

  const { can_use_premium_code, plan } = hello_dolly_editor_data;

  if (can_use_premium_code) {
    if (
      plan === 'summertime' ||
      plan === 'wonderful_world' ||
      plan === 'dream'
    ) {
      songs.push({ label: 'Summertime', value: 'Summertime' });
    }

    if (plan === 'wonderful_world' || plan === 'dream') {
      songs.push({ label: 'Wonderful World', value: 'Wonderful World' });
    }

    if (plan === 'dream') {
      songs.push({
        label: 'Dream a Little Dream',
        value: 'Dream a Little Dream',
      });
    }
  }

  return songs;
});
```

This won't do anything apart from filter which radio buttons are available in the block inspector panel. We also need to actively filter the lyrics for each song so that they're available in the paid plans.

First, add the filter as we did before:

[\[lyrics.js\]](https://github.com/Freemius/hello-dolly/blob/master/freemium%20v.3/hello-dolly/src/blocks/song-lyrics/lyrics.js#L35)

```javascript
lyrics = applyFilters('song-lyrics', lyrics);
```

And then extend the song lyrics too, similar to how we did before:

[\[extend-blocks.js\]](https://github.com/Freemius/hello-dolly/blob/master/freemium%20v.3/hello-dolly/src/pro/extend-blocks.js#L35-L133)

```javascript
addFilter('song-lyrics', 'hello-dolly/song-lyrics', function (lyrics) {
  if (!hello_dolly_editor_data) {
    return 'Error, Freemius data not found!';
  }

  const { can_use_premium_code, plan } = hello_dolly_editor_data;

  if (can_use_premium_code) {
    if (
      plan === 'summertime' ||
      plan === 'wonderful_world' ||
      plan === 'dream'
    ) {
      lyrics['Summertime'] = `Summertime and the livin' is easy
        ...
        Ah, said it's summertime`;
    }

    if (plan === 'wonderful_world' || plan === 'dream') {
      lyrics['Wonderful World'] = `I see trees of green, red roses, too,
        ...
        What a wonderful world`;
    }

    if (plan === 'dream') {
      lyrics['Dream a Little Dream'] = `Stars shining bright above you
        ...
        Dream a little dream of me`;
    }
  }

  return lyrics;
});
```

This works really well and all our paid features are completely stripped from the plugin during deployment.

You might have noticed that the JavaScript logic to check if the current active plan is valid is a little verbose:

```javascript
if (plan === 'summertime' || plan === 'wonderful_world' || plan === 'dream') {
  // add lyrics
}
```

Compared to it's PHP counterpart:

```php
if ( hd_fs()->is_plan( 'summertime' ) ) {
  // add lyrics
}
```

This is because we're localizing *just* the current active plan name and so more manual checks are required in the JavaScript code.

We could easily match the PHP logic by passing in more localized data to include specific plan data:

```php
$data = array(
  'current_plan'            => hd_fs()->get_plan_name(),
  'can_use_premium_code'    => hd_fs()->can_use_premium_code(),
  'is_plan_summertime'      => hd_fs()->is_plan( 'summertime' ),
  'is_plan_wonderful_world' => hd_fs()->is_plan( 'wonderful_world' ),
  'is_plan_dream'           => hd_fs()->is_plan( 'dream' ),
);

wp_localize_script('hello-dolly-block-script', 'hello_dolly_editor_data', $data);
```

And then changed the paid feature code to:

```javascript
addFilter('song-lyrics', 'hello-dolly/song-lyrics', function (lyrics) {
  if (!hello_dolly_editor_data) {
    return 'Error, Freemius data not found!';
  }

  const {
    can_use_premium_code,
    is_plan_summertime,
    is_plan_wonderful_world,
    is_plan_dream,
  } = hello_dolly_editor_data;

  if (can_use_premium_code) {
    if (is_plan_summertime) {
      lyrics['Summertime'] = `Summertime and the livin' is easy
        ...
        Ah, said it's summertime`;
    }

    if (is_plan_wonderful_world) {
      lyrics['Wonderful World'] = `I see trees of green, red roses, too,
        ...
        What a wonderful world`;
    }

    if (is_plan_dream) {
      lyrics['Dream a Little Dream'] = `Stars shining bright above you
      ...
      Dream a little dream of me`;
    }
  }
});
```

The system is quite flexible. You can choose which approach suits you best, you're not restricted to any particular implementation.

## Downgrading Issues[​](#downgrading-issues "Direct link to Downgrading Issues")

Sometimes when downgrading from the paid version to free you need to be aware of scenarios that could cause issues and unexpected behaviour in your blocks.

For example, in our Hello Dolly Freemium plugin if the currently selected song is only available in the paid version then it will suddenly disappear if the license is deactivated.

In this case we need to specifically reset the song and lyrics block attributes to the free one (Hello Dolly). Notice we're also resetting `lineNumber` as we can't guarantee the current line number will exist in Hello Dolly, and `showLineNumber` is reset too as this is a paid only feature.

```javascript
const {
  attributes: { song, lyric },
  setAttributes,
} = this.props;

// if downgrading and the currently selected song is not available
if (!lyrics.hasOwnProperty(song)) {
  setAttributes({
    song: 'Hello Dolly',
    lyric: lyrics['Hello Dolly'].split(/\n/)[0],
    lineNumber: 1,
    showLineNumber: false,
  });
}
```

## Deployment to Freemius[​](#deployment-to-freemius "Direct link to Deployment to Freemius")

Before deploying the plugin to Freemius make sure that you run the build script to produce compiled and minified block code.

Paid block features can be stripped out during deployment using the `@fs_premium_only` Freemius directive.

e.g. `@fs_premium_only /build/extend-blocks.js`

It's also recommended that you keep all your block source code in a single folder so that it can be easily removed prior to deployment if required.

## Testing the Hello Dolly Freemium Plugin[​](#testing-the-hello-dolly-freemium-plugin "Direct link to Testing the Hello Dolly Freemium Plugin")

The [Hello Dolly Freemium](https://github.com/Freemius/hello-dolly/tree/master/freemium%20v.3/hello-dolly) plugin contains a fully working example of a block integrated with the Freemius platform.

To install locally, clone the plugin repository: `git clone https://github.com/Freemius/hello-dolly.git`

The plugin uses the WordPress SDK as a submodule so you'll need to pull it after cloning using the following command: `git submodule update --init`

Then, copy the `freemium v.3\hello-dolly` folder to your local WordPress plugins folder (`/wp-content/plugins/`) and activate.

Upon activation we'll be prompted with a license activation screen. Since it's a Freemium plugin, you can click the *Activation Free Version* link to continue, and then choose whether to opt-in to Freemius usage-tracking or not.

To test the paid plans you can use the following license keys:

- *Summertime* plan license key: `sk_cOG+nk&tsEYLVo74~W*SqwJcLq4;V`
- *Wonderful World* plan license key: `sk_4#:r099AfRm8m*QUgN&K%s6Ds_Si5`
- *Dream* plan license key: `sk_6&Db*Nn#IVZ2oj7qh=ZHEkZv5H3a6`

If you already skipped the license activation prompt, a license can be activated from the plugins page in the WP Admin, by clicking the *Activate License* link under the **Hello Dolly Freemium** plugin.

To create and configure your own Hello Dolly Freemium plugin using Freemius from scratch, follow [this video tutorial](https://www.youtube.com/watch?v=gj6aoYG4fUI&t=101s) that takes you through the entire process step-by-step.

If you plan on making changes to blocks then use either of these two commands to recompile the block source code:

- Development: `npm run start:custom`
- Production: `npm run build:custom`