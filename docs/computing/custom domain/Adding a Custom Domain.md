# Adding a Custom Domain to Your Aleph.im Instance

Setting up a custom domain for your decentralized instance with Aleph.im can be accomplished with just a few steps. Please carefully follow this guide to ensure a smooth process.

## Overview

Adding a custom domain to your Aleph.im instance involves:

1. Creating a CNAME record.
2. Creating a TXT owner proof record.
3. Testing the domain setup.

This guide will take you through each step.

## Prerequisites

Before you start, make sure you have:

- Access to your domain's DNS settings.
- The Ethereum address you used to create the instance.


## Step 1: Create a CNAME Record

To add a custom domain, first, you need to create a CNAME record in your domain's DNS settings. The CNAME record will point your domain to your instance on Aleph.im.

1. **Log into your domain provider's site.**
2. **Navigate to your domain's DNS settings.** These settings are usually located in your domain control panel.
3. **Create a new CNAME record.**
   - For the `Name/Host/Alias` field, enter your domain (i.e., `<<userdomain.com>>`).
   - For the `Value/Answer/Destination` field, enter `program.public.aleph.sh`.

Your CNAME record should look something like this:

    NAME: <<userdomain.com>>
    VALUE: program.public.aleph.sh

Save your changes before moving on to the next step.


## Step 2: Create a TXT Owner Proof Record

Next, you need to create a TXT owner proof record in your domain's DNS settings. This record confirms that you own the domain associated with the Aleph.im instance.

1. **Still in your domain's DNS settings, create a new TXT record.**
   - For the `Name/Host/Alias` field, enter `_control.<<userdomain.com>>`.
   - For the `Value/Answer/Destination` field, enter your Ethereum address (i.e., `<<public address>>`).

Your TXT owner proof record should look something like this:

    NAME: _control.<<userdomain.com>>
    VALUE: <<public address>>

Save your changes before moving on to the next step.


## Step 3: Test the Domain Setup

After you've set up the DNS records, you can go to the domain detail page to check if the setup was successful.

1. **Navigate to the dashboard.**
2. **Select the domain you added.**
3. **Verify that all checks are successful.** 

