import json, re

BASE = "/Users/mrp/Documents/1-Projects/webscraping/nextjs-doc-scraper/docs/v16"

def slug(s):
    return re.sub(r'[^a-z0-9]+', '_', s.lower()).strip('_')

def path_slug(rel):
    # rel like "01-app/03-api-reference/07-adapters/06-implementing-ppr-in-an-adapter.mdx"
    noext = rel[:-4] if rel.endswith('.mdx') else rel
    return "docs_v16_" + slug(noext)

# (path_after docs/v16/, label, [(entity_slug, entity_label), ...])
docs = [
    ("01-app/03-api-reference/07-adapters/06-implementing-ppr-in-an-adapter.mdx", "Implementing PPR in an Adapter", [
        ("partial_prerendering", "Partial Prerendering (PPR)"),
        ("onbuildcomplete", "onBuildComplete hook"),
        ("fallback_shell", "Fallback shell + postponedState"),
        ("platform_cache", "Platform Cache"),
        ("oncacheentryv2", "requestMeta.onCacheEntryV2"),
        ("resume_protocol", "Resume protocol"),
        ("postponed_state", "Postponed state"),
    ]),
    ("01-app/03-api-reference/07-adapters/07-runtime-integration.mdx", "Runtime Integration", [
        ("deployment_adapter_api", "Deployment Adapter API (build-time)"),
        ("cachehandler", "cacheHandler runtime interface"),
        ("cachehandlers", "cacheHandlers runtime interface"),
        ("handler_context", "Handler Context"),
        ("waituntil", "ctx.waitUntil"),
        ("ppr_chain_headers", "PPR Chain Headers"),
        ("resume_protocol", "Resume protocol"),
    ]),
    ("01-app/03-api-reference/07-adapters/08-invoking-entrypoints.mdx", "Invoking Entrypoints", [
        ("handler_interface", "handler(req,res,ctx) interface"),
        ("nodejs_runtime_entrypoints", "Node.js runtime entrypoints"),
        ("edge_runtime_entrypoints", "Edge runtime entrypoints"),
        ("requestmeta", "requestMeta fields"),
        ("edge_entry_registry", "global edge entry registry (_ENTRIES)"),
        ("edgeRuntime_metadata", "output.edgeRuntime metadata"),
    ]),
    ("01-app/03-api-reference/07-adapters/09-output-types.mdx", "Output Types", [
        ("outputs_object", "outputs object"),
        ("pages_output", "outputs.pages"),
        ("pagesapi_output", "outputs.pagesApi"),
        ("apppages_output", "outputs.appPages"),
        ("approutes_output", "outputs.appRoutes"),
        ("prerenders_output", "outputs.prerenders"),
        ("staticfiles_output", "outputs.staticFiles"),
        ("middleware_output", "outputs.middleware"),
        ("edgeRuntime_metadata", "edgeRuntime"),
        ("output_export_mode", "output: 'export' mode"),
    ]),
    ("01-app/03-api-reference/07-adapters/10-routing-information.mdx", "Routing Information", [
        ("routing_object", "routing object"),
        ("beforemiddleware", "routing.beforeMiddleware"),
        ("beforefiles", "routing.beforeFiles"),
        ("afterfiles", "routing.afterFiles"),
        ("dynamicroutes_routing", "routing.dynamicRoutes"),
        ("onmatch", "routing.onMatch"),
        ("fallback_routing", "routing.fallback"),
        ("common_route_fields", "Common Route Fields"),
    ]),
    ("01-app/03-api-reference/07-adapters/11-use-cases.mdx", "Use Cases", [
        ("deployment_platform_integration", "Deployment Platform Integration"),
        ("asset_processing", "Asset Processing"),
        ("monitoring_integration", "Monitoring Integration"),
        ("custom_bundling", "Custom Bundling"),
        ("build_validation", "Build Validation"),
        ("route_generation", "Route Generation"),
    ]),
    ("01-app/03-api-reference/07-adapters/index.mdx", "Adapters", [
        ("deployment_adapters", "Build deployment adapters"),
        ("adapter_sections", "Adapter documentation sections"),
    ]),
    ("01-app/03-api-reference/07-edge.mdx", "Edge Runtime", [
        ("nodejs_runtime", "Node.js Runtime"),
        ("edge_runtime", "Edge Runtime"),
        ("edge_api_reference", "Edge Runtime API reference"),
        ("edge_caveats", "Edge Runtime caveats"),
        ("edge_network_apis", "Edge Network APIs"),
        ("edge_encoding_apis", "Edge Encoding APIs"),
        ("edge_stream_apis", "Edge Stream APIs"),
        ("edge_crypto_apis", "Edge Crypto APIs"),
        ("edge_web_standard_apis", "Edge Web Standard APIs"),
        ("edge_unsupported_apis", "Edge Unsupported APIs"),
        ("edge_environment_variables", "Edge Environment Variables"),
    ]),
    ("01-app/03-api-reference/08-turbopack.mdx", "Turbopack", [
        ("turbopack_bundler", "Turbopack incremental bundler"),
        ("unified_graph", "Unified Graph"),
        ("incremental_computation", "Incremental Computation"),
        ("lazy_bundling", "Lazy Bundling"),
        ("turbopack_supported_platforms", "Turbopack supported platforms"),
        ("default_bundler", "Turbopack default bundler"),
        ("wasm_fallback", "WASM fallback bindings"),
        ("turbopack_language_features", "Turbopack language features"),
        ("turbopack_css", "Turbopack CSS & styling"),
        ("turbopack_assets", "Turbopack assets"),
        ("turbopack_module_resolution", "Turbopack module resolution"),
        ("magic_comments", "Turbopack magic comments"),
        ("turbopack_webpack_gaps", "Turbopack vs webpack gaps"),
        ("turbopack_filesystem_cache", "Turbopack build caching"),
        ("turbopack_configuration", "Turbopack configuration"),
    ]),
    ("01-app/03-api-reference/index.mdx", "API Reference", [
        ("app_router_api_reference", "App Router API Reference"),
    ]),
    ("01-app/04-glossary.mdx", "Next.js Glossary", [
        ("glossary_app_router", "Glossary: App Router"),
        ("glossary_build_time", "Glossary: Build time"),
        ("glossary_cache_components", "Glossary: Cache Components"),
        ("glossary_client_component", "Glossary: Client Component"),
        ("glossary_client_cache", "Glossary: Client Cache"),
        ("glossary_hydration", "Glossary: Hydration"),
        ("glossary_isr", "Glossary: Incremental Static Regeneration (ISR)"),
        ("glossary_revalidation", "Glossary: Revalidation"),
        ("glossary_ppr", "Glossary: Partial Prerendering (PPR)"),
        ("glossary_rsc_payload", "Glossary: RSC Payload"),
        ("glossary_server_component", "Glossary: Server Component"),
        ("glossary_use_cache", "Glossary: \"use cache\" Directive"),
        ("glossary_use_client", "Glossary: \"use client\" Directive"),
        ("glossary_use_server", "Glossary: \"use server\" Directive"),
        ("glossary_streaming", "Glossary: Streaming"),
        ("glossary_suspense_boundary", "Glossary: Suspense boundary"),
        ("glossary_static_shell", "Glossary: Static Shell"),
        ("glossary_static_export", "Glossary: Static Export"),
        ("glossary_version_skew", "Glossary: Version skew"),
        ("glossary_turbopack", "Glossary: Turbopack"),
    ]),
    ("01-app/index.mdx", "App Router", [
        ("app_router", "App Router"),
    ]),
    ("02-pages/01-getting-started/01-installation.mdx", "Installation (Pages Router)", [
        ("pages_create_next_app", "create-next-app"),
        ("pages_typescript", "TypeScript setup"),
        ("pages_eslint", "ESLint setup"),
        ("pages_next_config", "next.config.js"),
        ("pages_router_installation", "Pages Router installation"),
    ]),
    ("02-pages/01-getting-started/02-project-structure.mdx", "Project Structure (Pages Router)", [
        ("pages_directory", "pages directory"),
        ("pages_project_structure", "Project Structure and Organization"),
        ("pages_file_conventions", "Pages file conventions"),
        ("pages_private_folders", "Private folders"),
        ("pages_dynamic_routes", "Dynamic routes"),
    ]),
    ("02-pages/01-getting-started/04-images.mdx", "Images (Pages Router)", [
        ("pages_next_image", "next/image component"),
        ("pages_image_optimization", "Image Optimization"),
        ("pages_image_api_reference", "Image API Reference"),
    ]),
    ("02-pages/01-getting-started/05-fonts.mdx", "Fonts (Pages Router)", [
        ("pages_next_font", "next/font"),
        ("pages_font_optimization", "Font Optimization"),
        ("pages_font_api_reference", "Font API Reference"),
    ]),
    ("02-pages/01-getting-started/06-css.mdx", "CSS (Pages Router)", [
        ("pages_css_modules", "CSS Modules"),
        ("pages_global_css", "Global CSS"),
        ("pages_tailwind_css", "Tailwind CSS"),
        ("pages_css_in_js", "CSS-in-JS"),
        ("pages_sass", "Sass"),
    ]),
    ("02-pages/01-getting-started/11-deploying.mdx", "Deploying (Pages Router)", [
        ("pages_deploying", "Deploying a Next.js application"),
    ]),
    ("02-pages/01-getting-started/index.mdx", "Getting Started - Pages Router", [
        ("pages_getting_started", "Pages Router Getting Started"),
    ]),
    ("02-pages/02-guides/analytics.mdx", "Analytics (Pages Router)", [
        ("pages_analytics", "Analytics"),
        ("pages_page_performance", "Page performance tracking"),
    ]),
    ("02-pages/02-guides/authentication.mdx", "Authentication (Pages Router)", [
        ("pages_authentication", "Authentication"),
        ("pages_session_management", "Session management"),
        ("pages_authorization", "Authorization"),
        ("pages_securing_routes", "Securing routes"),
    ]),
    ("02-pages/02-guides/babel.mdx", "Babel", [
        ("next_babel_preset", "next/babel preset"),
        ("babelrc", ".babelrc / babel.config.js"),
        ("babel_presets_plugins", "Babel presets and plugins"),
        ("babel_customizing", "Customizing Babel presets"),
        ("babel_preset_env", "preset-env modules option"),
    ]),
]

nodes = []
edges = []

for rel, label, concepts in docs:
    full = f"{BASE}/{rel}"
    pslug = path_slug(rel)
    doc_id = pslug
    nodes.append({
        "id": doc_id,
        "label": label,
        "file_type": "document",
        "source_file": full,
        "source_location": None,
        "source_url": None,
        "captured_at": None,
        "author": None,
        "contributor": None,
    })
    for eslug, elabel in concepts:
        nid = f"{pslug}_{eslug}"
        nodes.append({
            "id": nid,
            "label": elabel,
            "file_type": "concept",
            "source_file": full,
            "source_location": None,
            "source_url": None,
            "captured_at": None,
            "author": None,
            "contributor": None,
        })
        edges.append({
            "source": doc_id,
            "target": nid,
            "relation": "references",
            "confidence": "EXTRACTED",
            "confidence_score": 1.0,
            "source_file": full,
            "source_location": None,
            "weight": 1.0,
        })

# Cross-file semantically_similar_to INFERRED edges
similar = [
    ("docs_v16_01_app_03_api_reference_07_adapters_06_implementing_ppr_in_an_adapter_resume_protocol",
     "docs_v16_01_app_03_api_reference_07_adapters_07_runtime_integration_resume_protocol", 0.95),
    ("docs_v16_01_app_03_api_reference_07_adapters_06_implementing_ppr_in_an_adapter_partial_prerendering",
     "docs_v16_01_app_04_glossary_glossary_ppr", 0.95),
    ("docs_v16_01_app_03_api_reference_07_adapters_06_implementing_ppr_in_an_adapter_postponed_state",
     "docs_v16_01_app_04_glossary_glossary_suspense_boundary", 0.85),
    ("docs_v16_01_app_03_api_reference_07_adapters_07_runtime_integration_cachehandler",
     "docs_v16_01_app_04_glossary_glossary_static_export", 0.65),
    ("docs_v16_01_app_03_api_reference_07_adapters_08_invoking_entrypoints_edge_runtime_entrypoints",
     "docs_v16_01_app_03_api_reference_07_edge_edge_runtime", 0.95),
    ("docs_v16_01_app_03_api_reference_07_adapters_08_invoking_entrypoints_nodejs_runtime_entrypoints",
     "docs_v16_01_app_03_api_reference_07_edge_nodejs_runtime", 0.85),
    ("docs_v16_01_app_03_api_reference_07_adapters_09_output_types_prerenders_output",
     "docs_v16_01_app_03_api_reference_07_adapters_06_implementing_ppr_in_an_adapter_partial_prerendering", 0.85),
    ("docs_v16_01_app_03_api_reference_07_adapters_09_output_types_middleware_output",
     "docs_v16_01_app_03_api_reference_07_edge_edge_runtime", 0.75),
    ("docs_v16_01_app_03_api_reference_07_adapters_10_routing_information_routing_object",
     "docs_v16_01_app_03_api_reference_07_adapters_09_output_types_middleware_output", 0.65),
    ("docs_v16_01_app_03_api_reference_07_edge_edge_runtime",
     "docs_v16_01_app_03_api_reference_08_turbopack_turbopack_bundler", 0.55),
    ("docs_v16_01_app_03_api_reference_08_turbopack_turbopack_bundler",
     "docs_v16_01_app_04_glossary_glossary_turbopack", 0.95),
    ("docs_v16_01_app_03_api_reference_08_turbopack_default_bundler",
     "docs_v16_01_app_04_glossary_glossary_turbopack", 0.85),
    ("docs_v16_01_app_03_api_reference_08_turbopack_turbopack_css",
     "docs_v16_02_pages_01_getting_started_06_css_pages_css_modules", 0.75),
    ("docs_v16_01_app_04_glossary_glossary_app_router",
     "docs_v16_01_app_index_app_router", 0.95),
    ("docs_v16_01_app_04_glossary_glossary_server_component",
     "docs_v16_01_app_04_glossary_glossary_client_component", 0.85),
    ("docs_v16_01_app_04_glossary_glossary_use_cache",
     "docs_v16_01_app_04_glossary_glossary_cache_components", 0.85),
    ("docs_v16_01_app_04_glossary_glossary_streaming",
     "docs_v16_01_app_04_glossary_glossary_suspense_boundary", 0.85),
    ("docs_v16_01_app_04_glossary_glossary_static_shell",
     "docs_v16_01_app_04_glossary_glossary_ppr", 0.85),
    ("docs_v16_01_app_04_glossary_glossary_isr",
     "docs_v16_01_app_04_glossary_glossary_revalidation", 0.65),
    ("docs_v16_02_pages_01_getting_started_01_installation_pages_create_next_app",
     "docs_v16_01_app_04_glossary_glossary_hydration", 0.55),
    ("docs_v16_02_pages_01_getting_started_02_project_structure_pages_directory",
     "docs_v16_01_app_04_glossary_glossary_static_shell", 0.55),
    ("docs_v16_02_pages_02_guides_babel_babelrc",
     "docs_v16_01_app_03_api_reference_08_turbopack_turbopack_language_features", 0.65),
]

node_ids = {n["id"] for n in nodes}
for s, t, score in similar:
    if s in node_ids and t in node_ids:
        edges.append({
            "source": s,
            "target": t,
            "relation": "semantically_similar_to",
            "confidence": "INFERRED",
            "confidence_score": score,
            "source_file": nodes[0]["source_file"],
            "source_location": None,
            "weight": 1.0,
        })
    else:
        print("SKIP missing node:", s, t)

out = {
    "nodes": nodes,
    "edges": edges,
    "hyperedges": [],
    "input_tokens": 0,
    "output_tokens": 0,
}

target = "/Users/mrp/Documents/1-Projects/webscraping/nextjs-doc-scraper/graphify-out/.graphify_chunk_11.json"
with open(target, "w") as f:
    json.dump(out, f, indent=2)

print("nodes:", len(nodes))
print("edges:", len(edges))
print("docs:", len(docs))
