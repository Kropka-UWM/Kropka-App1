# frontend

## Project setup

Requires Node.js 24.15+ (24 LTS) or Node.js 26. Uses Vue 3, Vite, and Vitest.

```
npm ci
```

### Compiles and hot-reloads for development

```
npm run serve
```

### Compiles and minifies for production

```
npm run build
```

### Runs sample api server

```
npm run start
```

### Run your unit tests

```
npm run test:unit
```

### Lints files

```
npm run lint
```

### Customize configuration

Vite and Vitest are configured in `vite.config.mts`. ESLint uses `eslint.config.mjs`.
See the [Vite documentation](https://vite.dev/config/).

TypeScript is pinned to the compatible 6.0 line while typescript-eslint requires `<6.1`.
The Vuex path in `tsconfig.json` resolves its published types because Vuex 4's exports
do not expose them to TypeScript's bundler resolution.
