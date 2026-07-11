# Graph Report - .  (2026-07-11)

## Corpus Check
- cluster-only mode — file stats not available

## Summary
- 1224 nodes · 2857 edges · 46 communities
- Extraction: 94% EXTRACTED · 6% INFERRED · 0% AMBIGUOUS · INFERRED: 170 edges (avg confidence: 0.88)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `b1f7116b`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- Forms
- Avatar
- Components 9
- Components 2
- Breadcrumb
- Core Guides
- Sidebar
- Components 4
- Registry
- Authentication
- Hello World Block
- SidebarGroup
- Components 3
- SidebarProvider
- RTL Documentation
- Components 6
- Components 5
- Components 8
- Alert
- Field
- AlertDialog
- Tailwind v4
- ButtonGroup
- shadcn CLI
- ButtonGroupDemo
- components.json
- MCP & CLI
- Components 1
- Item
- Component List
- Theming Documentation
- Button Component
- Slider
- Installation
- SidebarMenuItem
- DropdownMenuContent
- Theming & RTL
- preset command
- Registry Getting Started
- Button
- Security Best Practices
- InputGroup
- registry.json
- AspectRatio
- v0 Open Endpoint
- Components 7

## God Nodes (most connected - your core abstractions)
1. `Core Guides` - 218 edges
2. `Registry` - 128 edges
3. `Components 1` - 119 edges
4. `Components 3` - 114 edges
5. `Components 4` - 77 edges
6. `Components 7` - 77 edges
7. `Components 2` - 76 edges
8. `Components 8` - 72 edges
9. `Components 5` - 68 edges
10. `Theming & RTL` - 65 edges

## Surprising Connections (you probably didn't know these)
- `Button` --semantically_similar_to--> `Button`  [AMBIGUOUS] [semantically similar]
  docs-components-tooltip.md → docs-dark-mode-astro.md
- `Button` --semantically_similar_to--> `Button`  [AMBIGUOUS] [semantically similar]
  docs-components-tooltip.md → docs-dark-mode-next.md
- `Button` --semantically_similar_to--> `Button`  [AMBIGUOUS] [semantically similar]
  docs-components-tooltip.md → docs-dark-mode-remix.md
- `Button` --semantically_similar_to--> `Button`  [AMBIGUOUS] [semantically similar]
  docs-components-tooltip.md → docs-dark-mode-vite.md
- `DropdownMenu` --semantically_similar_to--> `DropdownMenu`  [AMBIGUOUS] [semantically similar]
  docs-dark-mode-astro.md → docs-dark-mode-next.md

## Import Cycles
- None detected.

## Communities (46 total, 0 thin omitted)

### Community 0 - "Forms"
Cohesion: 0.08
Nodes (69): BugReportForm Component, Bug Report Form Action, Demo Form Action Function, CardRtl, BugReportForm Component, FormRhfInput Component, FormRhfTextarea Component, Formisch Documentation (+61 more)

### Community 1 - "Avatar"
Cohesion: 0.40
Nodes (15): Avatar, AvatarBadge, AvatarBadgeIconExample, AvatarDemo, AvatarFallback, AvatarGroup, AvatarGroupCount, AvatarGroupCountExample (+7 more)

### Community 2 - "Components 9"
Cohesion: 0.11
Nodes (46): ContextMenu, ContextMenuBasic, ContextMenuCheckboxes, ContextMenuCheckboxItem, ContextMenuContent, ContextMenuDemo, ContextMenuDestructive, ContextMenuItem (+38 more)

### Community 3 - "Components 2"
Cohesion: 0.06
Nodes (78): Button, Calendar, CalendarBasic, CalendarBookedDates, CalendarCaption, CalendarCustomDays, CalendarHijri, CalendarRange (+70 more)

### Community 4 - "Breadcrumb"
Cohesion: 0.30
Nodes (18): AvatarDropdown, Breadcrumb, BreadcrumbBasic, BreadcrumbDemo, BreadcrumbDropdown, BreadcrumbEllipsis, BreadcrumbEllipsisDemo, BreadcrumbItem (+10 more)

### Community 5 - "Core Guides"
Cohesion: 0.07
Nodes (54): Changelog, Context Menu Documentation, Data Table Documentation, Columns Definition, DataTable, Table, Translations, Forms (+46 more)

### Community 6 - "Sidebar"
Cohesion: 0.33
Nodes (7): ComponentSource, Sidebar, SidebarContent, SidebarFooter, SidebarHeader, SidebarMenu, SidebarRail

### Community 7 - "Components 4"
Cohesion: 0.06
Nodes (77): CopyIcon, ArrowUpRightIcon, Avatar, AvatarFallback, AvatarImage, Button, Empty, EmptyAvatar (+69 more)

### Community 8 - "Registry"
Cohesion: 0.08
Nodes (42): Alias Child, Alias Parent, Custom Style, Custom Theme, extractToken Function, Font JetBrains Mono, Font Lora, Font Playfair Display (+34 more)

### Community 9 - "Authentication"
Cohesion: 0.10
Nodes (20): API Key Authentication, authenticateUser Function, Error Handling, Express.js Example, getComponentsForTeam Function, getPersonalizedComponent Function, getTeamFromToken Function, getUserPreferences Function (+12 more)

### Community 10 - "Hello World Block"
Cohesion: 0.14
Nodes (18): Button Component, Components UI Registry JSON, Registry MCP Server, Format Date Utility, Formatted Message Component, Hello Config, Hello World Block, Hello World Component (+10 more)

### Community 11 - "SidebarGroup"
Cohesion: 0.29
Nodes (8): Collapsible, CollapsibleContent, CollapsibleTrigger, Plus, SidebarGroup, SidebarGroupAction, SidebarGroupContent, SidebarGroupLabel

### Community 12 - "Components 3"
Cohesion: 0.06
Nodes (107): Button, InputGroupAddon, Item, ItemContent, ItemDescription, ItemTitle, DirectionProvider, Translations (+99 more)

### Community 13 - "SidebarProvider"
Cohesion: 0.40
Nodes (5): PanelLeftIcon, SidebarInset, SidebarProvider, SidebarTrigger, useSidebar

### Community 14 - "RTL Documentation"
Cohesion: 0.17
Nodes (12): RTL Documentation, Calendar RTL Support, CLI RTL Transformation, Direction Component, DirectionProvider, Migration Guide, Next.js RTL Guide, Pagination RTL Support (+4 more)

### Community 15 - "Components 6"
Cohesion: 0.10
Nodes (49): Progress, ProgressControlled, ProgressDemo, ProgressRtl, ProgressWithLabel, Slider, useTranslation, Field (+41 more)

### Community 18 - "Components 5"
Cohesion: 0.08
Nodes (68): Badge, Button, Field, FieldDescription, FieldGroup, FieldLabel, Input, Select (+60 more)

### Community 19 - "Components 8"
Cohesion: 0.06
Nodes (66): Field, FieldContent, FieldDescription, FieldGroup, FieldLabel, FieldTitle, Label, Radix Switch (+58 more)

### Community 21 - "Alert"
Cohesion: 0.29
Nodes (15): Alert, AlertAction, AlertActionExample, AlertBasic, AlertCircleIcon, AlertColors, AlertDemo, AlertDescription (+7 more)

### Community 23 - "Field"
Cohesion: 0.11
Nodes (18): Checkbox, Field, FieldDescription, FieldError, FieldGroup, FieldLabel, FieldLegend, FieldSeparator (+10 more)

### Community 24 - "AlertDialog"
Cohesion: 0.42
Nodes (17): AlertDialog, AlertDialogBasic, AlertDialogCancel, AlertDialogContent, AlertDialogDemo, AlertDialogDescription, AlertDialogDestructive, AlertDialogFooter (+9 more)

### Community 26 - "Tailwind v4"
Cohesion: 0.15
Nodes (15): Astro, Gatsby, Laravel, Manual, Next.js, React 19, React Router, shadcn/ui (+7 more)

### Community 28 - "ButtonGroup"
Cohesion: 0.15
Nodes (23): Button, ButtonGroupInput, ButtonGroupNested, ButtonGroupOrientation, ButtonGroupSelect, ButtonGroupSeparator, Input, InputGroupAddon (+15 more)

### Community 29 - "shadcn CLI"
Cohesion: 0.09
Nodes (23): Accordion Component, AI-Ready Principle, Beautiful Defaults Principle, shadcn CLI, add command, apply command, build command, create command (+15 more)

### Community 31 - "ButtonGroupDemo"
Cohesion: 0.27
Nodes (13): ButtonGroupDemo, ButtonGroupRtl, DropdownMenu, DropdownMenuTrigger, ArchiveIcon, ArrowLeftIcon, CalendarPlusIcon, ClockIcon (+5 more)

### Community 32 - "components.json"
Cohesion: 0.18
Nodes (13): Authentication & Security, Central Open Source Registry Index, components.json, Configuration, Decentralized Namespace System, Dependency Resolution, Namespaces, Versioning (+5 more)

### Community 33 - "MCP & CLI"
Cohesion: 0.24
Nodes (16): Claude Code, Codex, components.json, Cursor, .mcp.json, MCP Server, Model Context Protocol (MCP), Namespaced Registries (+8 more)

### Community 34 - "Components 1"
Cohesion: 0.09
Nodes (44): Accordion, AccordionBasic, AccordionBorders, AccordionCard, AccordionContent, AccordionDemo, AccordionDisabled, AccordionItem (+36 more)

### Community 35 - "Item"
Cohesion: 0.18
Nodes (11): Field, Item, ItemActions, ItemContent, ItemDescription, ItemFooter, ItemGroup, ItemHeader (+3 more)

### Community 36 - "Component List"
Cohesion: 0.29
Nodes (11): shadcn CLI, Component List, Registry, Figma, Obra shadcn/ui Pro (Figma), shadcn/studio UI Kit (Figma), shadcn/ui components (Figma), shadcn/ui design system (Figma) (+3 more)

### Community 37 - "Theming Documentation"
Cohesion: 0.18
Nodes (11): Theming Documentation, Chart Theming Documentation, components.json, CSS Variables for Theming, Dark Mode Documentation, globals.css, Radius Scale, shadcn/create (+3 more)

### Community 38 - "Button Component"
Cohesion: 0.22
Nodes (10): Button Component, Custom Base, Custom Login, Example Style, Font Inter, Login 01 Block, My Design System, New Style (+2 more)

### Community 39 - "Slider"
Cohesion: 0.20
Nodes (10): Label, Slider, SliderControlled, SliderDemo, SliderDisabled, SliderMultiple, SliderRange, SliderRtl (+2 more)

### Community 40 - "Installation"
Cohesion: 0.07
Nodes (50): Astro Installation, Button Component, Gatsby, gatsby-node.ts, shadcn CLI, Tailwind CSS, TypeScript, Inertia (+42 more)

### Community 41 - "SidebarMenuItem"
Cohesion: 0.17
Nodes (13): ChevronDown, DropdownMenu, DropdownMenuContent, DropdownMenuItem, DropdownMenuTrigger, SidebarMenuAction, SidebarMenuBadge, SidebarMenuButton (+5 more)

### Community 42 - "DropdownMenuContent"
Cohesion: 0.22
Nodes (9): DropdownMenuContent, DropdownMenuGroup, DropdownMenuItem, DropdownMenuRadioGroup, DropdownMenuRadioItem, DropdownMenuSeparator, DropdownMenuSub, DropdownMenuSubContent (+1 more)

### Community 48 - "Theming & RTL"
Cohesion: 0.06
Nodes (66): components.json Configuration File, DirectionProvider Component, Astro Dark Mode, Button, DropdownMenu, DropdownMenuContent, DropdownMenuItem, DropdownMenuTrigger (+58 more)

### Community 49 - "preset command"
Cohesion: 0.33
Nodes (6): preset command, preset decode command, preset info command, preset open command, preset resolve command, preset url command

### Community 50 - "Registry Getting Started"
Cohesion: 0.22
Nodes (9): Registry FAQ, Registry Getting Started, GitHub Registries Documentation, Registry Index Documentation, Registry Item JSON Schema, Registry Item Schema Specification, Registry Schema Specification, Registry Template (+1 more)

### Community 54 - "Button"
Cohesion: 0.53
Nodes (6): Button, Sonner, SonnerDemo, SonnerDescription, SonnerPosition, SonnerTypes

### Community 57 - "Security Best Practices"
Cohesion: 0.25
Nodes (8): Access Logging, Environment Variables, generateToken Function, HTTPS, logAccess Function, Rate Limiting, Security Best Practices, Token Rotation

### Community 61 - "InputGroup"
Cohesion: 0.29
Nodes (7): Button, InputGroup, InputGroupAddon, InputGroupInput, Kbd, KbdGroup, Tooltip

### Community 66 - "registry.json"
Cohesion: 0.33
Nodes (6): registry.json, homepage (registry.json), include (registry.json), items (registry.json), name (registry.json), registry.json Schema

### Community 69 - "AspectRatio"
Cohesion: 0.50
Nodes (4): AspectRatio, AspectRatioDemo, AspectRatioPortrait, useTranslation

### Community 72 - "v0 Open Endpoint"
Cohesion: 0.67
Nodes (3): Open in v0, OpenInV0Button, v0 Open Endpoint

### Community 84 - "Components 7"
Cohesion: 0.09
Nodes (28): Button, Input, Label, Radix UI Dialog, Sheet, SheetClose, SheetContent, SheetDescription (+20 more)

## Ambiguous Edges - Review These
- `Field` → `FieldError`  [AMBIGUOUS]
  docs/components/label.md · relation: shares_data_with
- `Button` → `Button`  [AMBIGUOUS]
  docs-components-tooltip.md · relation: semantically_similar_to
- `Button` → `Button`  [AMBIGUOUS]
  docs-components-tooltip.md · relation: semantically_similar_to
- `Button` → `Button`  [AMBIGUOUS]
  docs-components-tooltip.md · relation: semantically_similar_to
- `Button` → `Button`  [AMBIGUOUS]
  docs-components-tooltip.md · relation: semantically_similar_to
- `DropdownMenu` → `DropdownMenu`  [AMBIGUOUS]
  docs-dark-mode-astro.md · relation: semantically_similar_to
- `DropdownMenu` → `DropdownMenu`  [AMBIGUOUS]
  docs-dark-mode-astro.md · relation: semantically_similar_to
- `DropdownMenu` → `DropdownMenu`  [AMBIGUOUS]
  docs-dark-mode-astro.md · relation: semantically_similar_to
- `Field Component (Formisch)` → `Field Component (shadcn)`  [AMBIGUOUS]
  docs-forms-formisch.md · relation: conceptually_related_to
- `formSchema (Zod)` → `FormRhfInput Component`  [AMBIGUOUS]
  docs-forms-react-hook-form.md · relation: references
- `formSchema (Zod)` → `FormRhfTextarea Component`  [AMBIGUOUS]
  docs-forms-react-hook-form.md · relation: references
- `New Style` → `Button Component`  [AMBIGUOUS]
  docs-registry-examples.md · relation: references
- `Custom Login` → `Button Component`  [AMBIGUOUS]
  docs-registry-examples.md · relation: references
- `Hello World Block` → `Button Component`  [AMBIGUOUS]
  docs-registry-getting-started.md · relation: references

## Knowledge Gaps
- **109 isolated node(s):** `Changelog`, `Translations`, `Badge`, `Spinner`, `ButtonGroup` (+104 more)
  These have ≤1 connection - possible missing edges or undocumented components.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **What is the exact relationship between `Field` and `FieldError`?**
  _Edge tagged AMBIGUOUS (relation: shares_data_with) - confidence is low._
- **What is the exact relationship between `Button` and `Button`?**
  _Edge tagged AMBIGUOUS (relation: semantically_similar_to) - confidence is low._
- **What is the exact relationship between `Button` and `Button`?**
  _Edge tagged AMBIGUOUS (relation: semantically_similar_to) - confidence is low._
- **What is the exact relationship between `Button` and `Button`?**
  _Edge tagged AMBIGUOUS (relation: semantically_similar_to) - confidence is low._
- **What is the exact relationship between `Button` and `Button`?**
  _Edge tagged AMBIGUOUS (relation: semantically_similar_to) - confidence is low._
- **What is the exact relationship between `DropdownMenu` and `DropdownMenu`?**
  _Edge tagged AMBIGUOUS (relation: semantically_similar_to) - confidence is low._
- **What is the exact relationship between `DropdownMenu` and `DropdownMenu`?**
  _Edge tagged AMBIGUOUS (relation: semantically_similar_to) - confidence is low._