---
title: React Reference Overview
---

<Intro>

This section provides detailed reference documentation for working with React. For an introduction to React, please visit the [Learn](learn.md) section.

</Intro>

The React reference documentation is broken down into functional subsections:

## React {/*react*/}

Programmatic React features:

* [Hooks](reference-react-hooks.md) - Use different React features from your components.
* [Components](reference-react-components.md) - Built-in components that you can use in your JSX.
* [APIs](reference-react-apis.md) - APIs that are useful for defining components.
* [Directives](reference-rsc-directives.md) - Provide instructions to bundlers compatible with React Server Components.

## React DOM {/*react-dom*/}

React DOM contains features that are only supported for web applications (which run in the browser DOM environment). This section is broken into the following:

* [Hooks](reference-react-dom-hooks.md) - Hooks for web applications which run in the browser DOM environment.
* [Components](reference-react-dom-components.md) - React supports all of the browser built-in HTML and SVG components.
* [APIs](reference-react-dom.md) - The `react-dom` package contains methods supported only in web applications.
* [Client APIs](reference-react-dom-client.md) - The `react-dom/client` APIs let you render React components on the client (in the browser).
* [Server APIs](reference-react-dom-server.md) - The `react-dom/server` APIs let you render React components to HTML on the server.
* [Static APIs](reference-react-dom-static.md) - The `react-dom/static` APIs let you generate static HTML for React components.

## React Compiler {/*react-compiler*/}

The React Compiler is a build-time optimization tool that automatically memoizes your React components and values:

* [Configuration](reference-react-compiler-configuration.md) - Configuration options for React Compiler.
* [Directives](reference-react-compiler-directives.md) - Function-level directives to control compilation.
* [Compiling Libraries](reference-react-compiler-compiling-libraries.md) - Guide for shipping pre-compiled library code.

## ESLint Plugin React Hooks {/*eslint-plugin-react-hooks*/}

The [ESLint plugin for React Hooks](reference-eslint-plugin-react-hooks.md) helps enforce the Rules of React:

* [Lints](reference-eslint-plugin-react-hooks.md) - Detailed documentation for each lint with examples.

## Rules of React {/*rules-of-react*/}

React has idioms — or rules — for how to express patterns in a way that is easy to understand and yields high-quality applications:

* [Components and Hooks must be pure](reference-rules-components-and-hooks-must-be-pure.md) – Purity makes your code easier to understand, debug, and allows React to automatically optimize your components and hooks correctly.
* [React calls Components and Hooks](reference-rules-react-calls-components-and-hooks.md) – React is responsible for rendering components and hooks when necessary to optimize the user experience.
* [Rules of Hooks](reference-rules-rules-of-hooks.md) – Hooks are defined using JavaScript functions, but they represent a special type of reusable UI logic with restrictions on where they can be called.

## Legacy APIs {/*legacy-apis*/}

* [Legacy APIs](reference-react-legacy.md) - Exported from the `react` package, but not recommended for use in newly written code.

---

## Sitemap

[Overview of all docs pages](/llms.txt)
