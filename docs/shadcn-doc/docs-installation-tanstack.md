Install and configure shadcn/ui for TanStack Start.

Choose the setup that matches your starting point.

## [Use shadcn/create](#use-shadcncreate)

### [Build Your Preset](#build-your-preset)

Open [shadcn/create](https://ui.shadcn.com/create?template=start) and build your preset visually. Choose your style, colors, fonts, icons, and more.

[Open shadcn/create](https://ui.shadcn.com/create?template=start)

### [Create Project](#create-project)

Click `Create Project`, choose your package manager, and copy the generated command.

The generated command will look similar to this:

```

```

The exact command will include your selected options such as `--base`, `--monorepo`, or `--rtl`.

### [Add Components](#add-components)

Add the `Card` component to your project:

```

```

If you created a monorepo, run the command from `apps/web` or specify the workspace from the repo root:

```

```

The command above will add the `Card` component to your project. You can then import it like this:

src/routes/index.tsx

```
import { createFileRoute } from "@tanstack/react-router"
 
import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from "@/components/ui/card"
 
export const Route = createFileRoute("/")({
  component: App,
})
 
function App() {
  return (
    <Card className="max-w-sm">
      <CardHeader>
        <CardTitle>Project Overview</CardTitle>
        <CardDescription>
          Track progress and recent activity for your TanStack Start app.
        </CardDescription>
      </CardHeader>
      <CardContent>
        Your design system is ready. Start building your next component.
      </CardContent>
    </Card>
  )
}
```

If you created a monorepo, update `apps/web/src/routes/index.tsx` and import from `@workspace/ui/components/card` instead.

## [Use the CLI](#use-the-cli)

### [Create Project](#create-project-1)

Run the `init` command to scaffold a new TanStack Start project. Follow the prompts to configure your project: base, preset, monorepo, and more.

```

```

**For a monorepo project, use `--monorepo` flag:**

```

```

### [Add Components](#add-components-1)

Add the `Card` component to your project:

```

```

If you created a monorepo, run the command from `apps/web` or specify the workspace from the repo root:

```

```

The command above will add the `Card` component to your project. You can then import it like this:

src/routes/index.tsx

```
import { createFileRoute } from "@tanstack/react-router"
 
import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from "@/components/ui/card"
 
export const Route = createFileRoute("/")({
  component: App,
})
 
function App() {
  return (
    <Card className="max-w-sm">
      <CardHeader>
        <CardTitle>Project Overview</CardTitle>
        <CardDescription>
          Track progress and recent activity for your TanStack Start app.
        </CardDescription>
      </CardHeader>
      <CardContent>
        Your design system is ready. Start building your next component.
      </CardContent>
    </Card>
  )
}
```

If you created a monorepo, update `apps/web/src/routes/index.tsx` and import from `@workspace/ui/components/card` instead.

## [Existing Project](#existing-project)

### [Create Project](#create-project-2)

If you need a new TanStack Start project, create one first. Otherwise, skip this step.

```

```

Choose TanStack Start, the React framework, and the recommended defaults so Tailwind CSS and the `@/*` import alias are configured for you.

Do not add the `shadcn` add-on when prompted. The `shadcn` CLI will configure shadcn/ui later in this guide.

The TanStack CLI already configures Tailwind CSS and the default `@/*` import alias for you. If you're adding shadcn/ui to an older or custom TanStack Start app, make sure both are configured before continuing.

### [Run the CLI](#run-the-cli)

Run the `shadcn` init command to set up shadcn/ui in your project.

```

```

### [Add Components](#add-components-2)

You can now start adding components to your project.

```

```

The command above will add the `Button` component to your project. You can then import it like this:

src/routes/index.tsx

```
import { createFileRoute } from "@tanstack/react-router"
 
import { Button } from "@/components/ui/button"
 
export const Route = createFileRoute("/")({
  component: App,
})
 
function App() {
  return (
    <div className="flex min-h-svh items-center justify-center p-6">
      <Button>Click me</Button>
    </div>
  )
}
```

[Astro](docs-installation-astro.md)[TanStack Router](docs-installation-tanstack-router.md)