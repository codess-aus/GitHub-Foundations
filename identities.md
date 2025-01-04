# Authenticate and authorize user identities on GitHub

An important component of an enterprise security strategy is **SAML SSO**. It provides a link between the IdP authorization and access to service providers (SaaS). This form of authentication allows users to sign in to all their applications with one set of credentials. Through SAML, the IdP authenticates users and grants authorization to services like GitHub. When a user logs in to GitHub, they can view the enterprises of which they're members. However, if the user tries to access repository data, GitHub will prompt for enterprise credentials (Enterprise ID).

With **security keys**, your enterprise can achieve a higher level of user security and protection. With two-factor authentication enabled, security keys provide a strong, convenient, and phishing-proof option for 2FA. Authentication with a security key requires that TOTP (Time-based one-time password) or SMS authentication has already been completed. On most devices, you can use a physical security key over USB or NFC. A user can register a new security key by accessing their profile setting and following the security key’s documentation. Using **these keys is the most secure form of 2FA**, because they're nearly impossible for a malicious party to replicate.

## What type of user authentication is used to verify a user identity against a known identity provider? 

Two-factor authentication (2FA)

Time-based One-time Password (TOTP)

**SAML Single Sign-on (SAML SSO)**
SAML authentication is a process used to verify user identity and credentials against a known identify provider.

Short Message Service (SMS)

## You're an admin and want to enable team synchronization for your organization. What installation permissions do you need to configure team synchronization for Microsoft Entra ID? 

Provide the tenant URL

**Read all users' full profiles**
To enable team synchronization for Microsoft Entra ID, the installation needs the following permissions: read all users' full profiles, sign in and read user profile, and read directory data.

Generate a valid Single Sign-on for Web Systems (SSWS) token

Enable SAML Single Sign-on (SSO)

## Where does a user authenticate after enabling SAML Single sign-on? 

With a GitHub login

With the organization credentials

**With the Identity Provider (IdP)**
When a member accesses resources within an organization that uses SAML SSO, GitHub redirects the member to the IdP to authenticate.

## What two-factor authentication method supports the secure backup of your authentication codes in the cloud? 

**Time-based One-time Password (TOTP)**
TOTP apps support the secure backup of your authentication codes in the cloud, and can be restored if you lose access to your device.

Short Message Service (SMS)

Security Key

Here are some links to more detailed information on the topics we discussed in this module:

[Managing SAML single sign-on for your organization](https://docs.github.com/enterprise-cloud@latest/organizations/managing-saml-single-sign-on-for-your-organization)
[Viewing and managing a member's SAML access to your organization](https://docs.github.com/enterprise-cloud@latest/organizations/granting-access-to-your-organization-with-saml-single-sign-on/viewing-and-managing-a-members-saml-access-to-your-organization)
[Preparing to require two-factor authentication in your organization](https://docs.github.com/organizations/keeping-your-organization-secure/managing-two-factor-authentication-for-your-organization/preparing-to-require-two-factor-authentication-in-your-organization)
[Authorizing a personal access token for use with SAML single sign-on](https://docs.github.com/enterprise-cloud@latest/authentication/authenticating-with-saml-single-sign-on/authorizing-a-personal-access-token-for-use-with-saml-single-sign-on)
[Authorizing an SSH key for use with SAML single sign-on](https://docs.github.com/enterprise-cloud@latest/authentication/authenticating-with-saml-single-sign-on/authorizing-an-ssh-key-for-use-with-saml-single-sign-on)
[Synchronizing a team with an identity provider](https://docs.github.com/enterprise-cloud@latest/organizations/organizing-members-into-teams/synchronizing-a-team-with-an-identity-provider-group)
