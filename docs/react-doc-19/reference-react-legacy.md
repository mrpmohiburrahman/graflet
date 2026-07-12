---
title: "Legacy React APIs"
---

<Intro>

These APIs are exported from the `react` package, but they are not recommended for use in newly written code. See the linked individual API pages for the suggested alternatives.

</Intro>

---

## Legacy APIs {/*legacy-apis*/}

* [`Children`](reference-react-Children.md) lets you manipulate and transform the JSX received as the `children` prop. [See alternatives.](reference-react-Children.md#alternatives)
* [`cloneElement`](reference-react-cloneElement.md) lets you create a React element using another element as a starting point. [See alternatives.](reference-react-cloneElement.md#alternatives)
* [`Component`](reference-react-Component.md) lets you define a React component as a JavaScript class. [See alternatives.](reference-react-Component.md#alternatives)
* [`createElement`](reference-react-createElement.md) lets you create a React element. Typically, you'll use JSX instead.
* [`createRef`](reference-react-createRef.md) creates a ref object which can contain arbitrary value. [See alternatives.](reference-react-createRef.md#alternatives)
* [`forwardRef`](reference-react-forwardRef.md) lets your component expose a DOM node to parent component with a [ref.](learn-manipulating-the-dom-with-refs.md)
* [`isValidElement`](reference-react-isValidElement.md) checks whether a value is a React element. Typically used with [`cloneElement`.](reference-react-cloneElement.md)
* [`PureComponent`](reference-react-PureComponent.md) is similar to [`Component`,](reference-react-Component.md) but it skip re-renders with same props. [See alternatives.](reference-react-PureComponent.md#alternatives)

---

## Removed APIs {/*removed-apis*/}

These APIs were removed in React 19:

* [`createFactory`](https://18.react.dev/reference/react/createFactory): use JSX instead.
* Class Components: [`static contextTypes`](https://18.react.dev//reference/react/Component#static-contexttypes): use [`static contextType`](#static-contexttype) instead.
* Class Components: [`static childContextTypes`](https://18.react.dev//reference/react/Component#static-childcontexttypes): use [`static contextType`](#static-contexttype) instead.
* Class Components: [`static getChildContext`](https://18.react.dev//reference/react/Component#getchildcontext): use [`Context`](reference-react-createContext.md#provider) instead.
* Class Components: [`static propTypes`](https://18.react.dev//reference/react/Component#static-proptypes): use a type system like [TypeScript](https://www.typescriptlang.org/) instead.
* Class Components: [`this.refs`](https://18.react.dev//reference/react/Component#refs): use [`createRef`](reference-react-createRef.md) instead.

---

## Sitemap

[Overview of all docs pages](/llms.txt)
