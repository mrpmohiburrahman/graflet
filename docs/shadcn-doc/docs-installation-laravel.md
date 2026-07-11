Install and configure shadcn/ui for Laravel.

The shadcn CLI does not scaffold a new Laravel app. Start by creating a Laravel app with the React starter kit, then choose how you want to configure shadcn/ui.

### [Create Project](#create-project)

Create a new Laravel app using the Laravel installer:

```
laravel new my-app
```

If you already have a Laravel app with React and Inertia configured, skip this step.

Choose the **React** starter kit when prompted. For more information, see the official [Laravel frontend documentation](https://laravel.com/docs/12.x/frontend).

Then move into your project directory:

```
cd my-app
```

## [Use shadcn/create](#use-shadcncreate)

### [Build Your Preset](#build-your-preset)

Open [shadcn/create](https://ui.shadcn.com/create?template=laravel) and build your preset visually. Choose your style, colors, fonts, icons, and more.

[Open shadcn/create](https://ui.shadcn.com/create?template=laravel)

### [Run the Command](#run-the-command)

Click `Create Project`, choose your package manager, and copy the generated command.

The generated command will look similar to this:

```

```

Run the command from the root of your Laravel app.

When asked to overwrite `components.json` and components, choose `Yes`.

### [Add Components](#add-components)

Add the `Switch` component to your project:

```

```

The command above will add the `Switch` component to `resources/js/components/ui/switch.tsx`. You can then import it like this:

resources/js/pages/index.tsx

```
import { Switch } from "@/components/ui/switch"
 
const MyPage = () => {
  return (
    <div>
      <Switch />
    </div>
  )
}
 
export default MyPage
```

## [Use the CLI](#use-the-cli)

### [Run the CLI](#run-the-cli)

Run the `shadcn` init command from the root of your Laravel app:

```

```

When asked to overwrite `components.json` and components, choose `Yes`.

### [Add Components](#add-components-1)

Add the `Switch` component to your project:

```

```

The command above will add the `Switch` component to `resources/js/components/ui/switch.tsx`. You can then import it like this:

resources/js/pages/index.tsx

```
import { Switch } from "@/components/ui/switch"
 
const MyPage = () => {
  return (
    <div>
      <Switch />
    </div>
  )
}
 
export default MyPage
```

[Vite](docs-installation-vite.md)[React Router](docs-installation-react-router.md)