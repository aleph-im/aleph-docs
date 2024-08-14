# Web3 Hosting on Aleph.im

## Overview

Aleph.im offers web3 hosting services via the [Twentysix Cloud Console](https://console.twentysix.cloud/), allowing you to deploy any kind of Dapps in few simple steps. Your websites are stored on IPFS and are fully-managed by the Aleph network.

Aleph.im being GDPR-compliant, if you decide to delete your website, or some older versions of it (previous deployments), or if you stop holding the required amount of tokens to keep it online, your website will be automatically garbage collected after a grace period by our network.

> Note: IPFS being a public P2P network, your files may still be available over the network if external IPFS nodes pinned them.

## Getting started

### Prepare

You just need to provide the root folder containing your static website's files.

#### Simple Static Website

The minimal requirement is that your folder must contain an `index.html` file. This file will always be the entry point of your website.

```bash
static-folder
├── index.html [required]
├── style.css
├── script.js
├── assets
:   └── ...
```

#### Framework-based Website

We are listing the officially supported frameworks on TwentySix's website creation page, but you can actually use any framework (and package manager, such as npm, pnpm, yarn, bun...) to create your website.

> Note: Keep in mine that your website must only contain client-side components, as well as the dependencies used by it. For backend support, check out the section below.

### Build

When your project is ready, you can build and generate your static folder.
Example using npm:
```bash
npm install
npm run build
```

> Note: The name of the output folder depends on the framework, it's usually `out` or `dist`.

### Deploy

TODO: aleph-client commands / 26-cloud screenshots

### History

TODO: Manage the previous versions of your website

## Access Your Dapp

### Aleph Gateway Service

When your website is live on Aleph network, we provide you a gateway url to easily access it:
`https://{ipfs-cid-v1}.ipfs.aleph.sh`

You can also access it in a similar fashion using alternative gateways, since your website is hosted on IPFS.
Find alternative gateways [here](https://ipfs.github.io/public-gateway-checker/).

### Custom Domains

TODO: some details + link to docs page

### ENS Domains

Since your website is hosted on IPFS, we are compatible with the ENS standard.<br>
To make it usable with ENS resolver such as:

`https://{your-ens-name}.eth.limo`<br>
or<br>
`https://{your-ens-name}.eth.link`

You need to setup the content hash field of your ENS with:<br>
`ipfs://{ipfs-cid-v1}`

Aleph is not compatible with IPNS, allowing you update automatically the live version of your dapp.
We are planning to support it in the near future, and we are working on building our own Aleph-native alternative to Limo, which is currently not a decentralized and scalable service.

## Advanced Features

### Handle Redirections on IPFS

By default, IPFS can't handle any fallback redirections.
To do so, you should add a `_redirects` file into your dapp structure.

For simple website, it should be located in the root folder.
For framework-based website, it should be located in the `public` folder.
Then at build time, it will be moved at the root.
Check out the documentation for more details.

#### Useful Links
- [IPFS docs](https://docs.ipfs.tech/how-to/websites-on-ipfs/redirects-and-custom-404s/)
- [Specifications](https://specs.ipfs.tech/http-gateways/web-redirects-file/)

### Backend Support

In order to add a backend to your website and to make it a real fullstack dapp,
there are 2 current approchs you can implement:

- Deploy your backend as a function, using our serverless solution.
- Deploy your instance, setup your environment, and expose your APIs to the internet.

> Note: You should setup your backend in advance, in order to integrate the needed endpoint urls inside your website later.

### Auto-Deployment on Push

Coming soon...

## Special Framework Requirements

### Vite with aleph-sdk-ts

In order to build a Vite Dapp using aleph-sdk-ts, follow the instructions on [this page](../libraries/typescript-sdk/troubleshooting.md)