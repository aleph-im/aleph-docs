# Troubleshooting Guide

## Wagmi-compatible Web3Provider

The SDK is based on Ethers, if you are using Wagmi instead, a quick setup is required.
You can use this function to obtain a compatible Web3Provider:

```typescript
import { providers } from "ethers";
import type { Account, Chain, Client, Transport } from "viem";
import { useConnectorClient } from "wagmi";

export function clientToSigner(client: Client<Transport, Chain, Account>) {
  const { account, chain, transport } = client;
  const network = {
    chainId: chain.id,
    name: chain.name,
    ensAddress: chain.contracts?.ensRegistry?.address,
  };
  const provider = new providers.Web3Provider(transport, network);
  // Uncomment next line if you want to load a specific wallet address beforehand
  // provider.getSigner(account.address);
  return provider;
}

export function useEtherProvider() {
  const { data: client } = useConnectorClient();
  if (!client) {
    return;
  }
  return clientToSigner(client);
}
```

## Vite: Module externalized for browser compatibility

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
import { defineConfig } from "vite";
import { nodePolyfills } from "vite-plugin-node-polyfills";

export default defineConfig({
  plugins: [nodePolyfills()],
});
```

## Found an issue?

If the documentation didn't help, you can [report an issue](https://github.com/aleph-im/support/issues).
