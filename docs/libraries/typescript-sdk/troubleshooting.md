# Troubleshooting Guide

As of now, the SDK is in beta and we are working on improving it.
If you encounter any issues, please let us know by creating an issue on the [GitHub repository](https://github.com/aleph-im/aleph-sdk-ts/issues).

## 1. Vite: Module externalized for browser compatibility

If you are using the SDK in a browser environment, you may encounter the following error:

```plaintext
Module "buffer" has been externalized for browser compatibility.
Cannot access "buffer.Buffer" in client code.
See https://vitejs.dev/guide/troubleshooting.html#module-externalized-for-browser-compatibility for more details.
```

Even though the SDK is designed to work in both Node.js and browser environments, the Vite bundler may throw this error.
To fix it, you can install [this Vite plugin for polyfilling Node.js built-in modules](https://www.npmjs.com/package/vite-plugin-node-polyfills):

```shell
npm i vite-plugin-node-polyfills
```

Then, add the plugin to your `vite.config.js`:

```javascript
import { defineConfig } from 'vite'
import { nodePolyfills } from 'vite-plugin-node-polyfills'

export default defineConfig({
  plugins: [
    nodePolyfills(),
  ],
});
```
