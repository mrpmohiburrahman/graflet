---
title: "Changing the Text or Language of the Components"
url: "https://freemius.com/help/documentation/saas-sdk/react-starter/localization/"
source: "docs"
section: "Docs"
category: "SDKs & Starter Kits"
scraped_at: "2026-04-09T19:58:41+06:00"
word_count: 404
---

All React Starter Kit components use a `LocaleProvider` context to manage the text they display. You can find the provider in the `react-starter/utils/locale.tsx` file ([source code](https://github.com/Freemius/freemius-js/blob/main/packages/saas-kit/registry/saas-kit/utils/locale.tsx)).

We recommend the following approach to change the text or language of the components:

## Wrap your app with the `LocaleProvider`[​](#wrap-your-app-with-the-localeprovider "Direct link to wrap-your-app-with-the-localeprovider")

```tsx
import {
  LocaleProvider,
  type LocaleType,
  defaultLocale,
} from '@/react-starter/utils/locale';

const overrides: Partial<LocaleType> = {
  checkout: {
    ...defaultLocale.checkout,
    processing: () => <>Processing... Please wait.</>,
  },
};

export default function App() {
  return (
    <LocaleProvider overrides={overrides}>
      {/* Your app components */}
    </LocaleProvider>
  );
}
```

This way, you can use the default locale and override only the strings or fragments you want to change.

tip

You will notice that most locale strings are JSX elements (e.g., `React.ReactNode`), not just plain strings. This allows for greater flexibility, such as adding links or formatting.

## Using a Translation Library[​](#using-a-translation-library "Direct link to Using a Translation Library")

Because the locale strings are JSX elements, you can easily integrate any translation library of your choice. Here are examples with the popular [lingui](https://lingui.dev/tutorials/react/) and [react-i18next](https://react.i18next.com/getting-started) libraries.

- lingui
- react-18next

```tsx
import { Trans } from '@lingui/react/macro';
import {
  LocaleProvider,
  type LocaleType,
  defaultLocale,
} from '@/react-starter/utils/locale';

const overrides: Partial<LocaleType> = {
  checkout: {
    ...defaultLocale.checkout,
    processing: () => <Trans>Processing... Please wait.</Trans>,
  },
};
```

Now you can use the `lingui` CLI tools to [extract](https://lingui.dev/ref/cli#extract) and manage your translations.

For the react-i18next example, you can use the `useTranslation` hook to get the `t` function and translate the strings. Note that we use the `useMemo` hook to avoid unnecessary re-renders.

```tsx
import { useTranslation } from 'react-i18next';
import * as React from 'react';
import {
  LocaleProvider,
  type LocaleType,
  defaultLocale,
} from '@/react-starter/utils/locale';

export default function App() {
  const { t } = useTranslation();

  const overrides: Partial<LocaleType> = React.useMemo(
    () => ({
      checkout: {
        ...defaultLocale.checkout,
        processing: () => <>{t('Processing... Please wait.')}</>,
      },
    }),
    [t, defaultLocale]
  );

  return (
    <LocaleProvider overrides={overrides}>
      {/* Your app components */}
    </LocaleProvider>
  );
}
```

## Editing the Component Source Code[​](#editing-the-component-source-code "Direct link to Editing the Component Source Code")

warning

This approach is not recommended, as it will make it more difficult to update the components in the future.

If, for some reason, you cannot use the `LocaleProvider`, you can edit the source code of the components directly. The starter kit is based on [shadcn/ui](https://ui.shadcn.com/), so you will receive the actual component files that you can customize as needed.