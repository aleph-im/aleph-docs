# How to host a static website using aleph.im?

## Introduction

### What is IPFS?

Aleph.im uses [InterPlanetary File System (IPFS)](https://ipfs.tech/), a mature, production-ready open source project that aims to revolutionize the way we store, access, and share information on the web. Born in 2014, IPFS has been developed by a large and active community of contributors, and has already been adopted by a wide range of organizations and projects.

IPFS is designed to address some of the most pressing challenges facing the web today, including issues of centralization, scalability, and censorship resistance. By providing a distributed, peer-to-peer network for storing and sharing content, IPFS offers a powerful alternative to traditional HTTP-based systems, and has the potential to be one of the next major trends in web development.

In IPFS, files are stored using a content-addressed system, where each file is identified by its unique content hash. When you request a file on the IPFS network, your node will look for other nodes on the network that are currently storing a copy of the file based on its hash.

### What is the service provided by aleph.im on top of IPFS?

If no nodes are currently storing the file, your node will not be able to retrieve it. **This is where Aleph.im pinning service comes in** - by pinning a file, you're telling a node to keep a copy of the file permanently, so that it's always available on the network. If a file is not pinned, it may be removed from the network if no other nodes are storing it, making it difficult or impossible to access in the future.

### Why should you consider deploying your website on IPFS?

IPFS provides several benefits over traditional hosting methods. For instance, hosting a website on IPFS can increase security by distributing the content across a network of nodes, making it harder for hackers or other malicious actors to take down or compromise the website. Additionally, IPFS is resistant to censorship and provides a way to publish content without relying on a centralized authority, making it ideal for those who want to ensure their content can be accessed freely. Finally, IPFS can improve the availability of a website by storing the content on multiple nodes, so if one node goes offline, the content can still be accessed from another node.

The main downside of IPFS hosting is that while IPFS itself is an open-source protocol, deploying a website on IPFS may require the use of third-party tools or services, such as IPFS gateways or DNS providers. This can introduce additional complexity and potential points of failure. Although if you can read those docs this means your browser can access IPFS without additional configuration (as these are hosted on IPFS as well).

Another important thing to keep in mind when using IPFS for hosting a static website is that the content is referenced by an immutable hash, which means that any changes to the content will result in a new hash. This means that if you want to update your website, you will need to redeploy the entire site and generate a new hash for the updated content. While this may be less convenient than making incremental updates to a traditional website, it does ensure that the content is tamper-proof and resistant to censorship.

## Deploy

To host a static website on IPFS, you would need to first create the website as a collection of static files (HTML, CSS, JavaScript, images, etc.). Once your website is ready, there are several options to host it on IPFS using the Aleph Node as a pinning service to persist your data.

### Requirements

### Deploy using the aleph.im Account dApp

### Deploy using the aleph.im command line interface (CLI)

### Deploy using one of the aleph.im SDK
