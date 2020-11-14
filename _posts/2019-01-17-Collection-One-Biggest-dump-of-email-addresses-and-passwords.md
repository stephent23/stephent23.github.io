---
type: posts
title: Collection 1 - What should you do? 
tags: [Passwords, Breaches, Compromise, Identity]
category: Breaches
toc: true
---

### What is collection #1?
Simply put, this is a huge set of data which contains more than 1.1 billion unique email address and password combinations. The dataset is made up of many smaller data breaches however, the source of these are not known. 

This presents a challenge if we appear in the dataset, as how do we know what online services to reset our password on? The short answer is, we don't know and in truth, we are unlikely to do so in the near future, if ever at all. However, it is fair to assume that they are from a combination of different online services, anything from forums to online retailers.

### How do I know if I am affected? 
This is simple thanks to the service <a href="https://haveibeenpwned.com">haveibeenpwned.com</a>, created by <a href="https://twitter.com/troyhunt">@troyhunt</a>. Type in your email address and you will be able to see if it appears in the Collection #1 dataset. If you have, you'll see an entry exactly like the one below:
<br />
<br />
![Collection 1 HaveIBeenPwned Screenshot](/assets/img/custom/posts/haveibeenpwned_collection1.png)

### What is the risk? 
Hackers or criminal organisations are able to perform account takeovers utilising datasets such as Collection #1 in an automated way. This simple, yet increasingly common method of online account compromise is known as Credential Stuffing and is described as the *"automated injection of breached username/password pairs in order to fraudulently gain access to user accounts"* [1]. 

In essence the risk to us depends on the extent to which we re-use our passwords. If you re-use the same email address and password combinations across many online services, then the risk is relatively high compared to if you use a different password for each online service that you sign up for. If you do re-use passwords across the majority of your online services, then you should probably take some action - see below.

### I'm affected - What should I do?
If you re-use the same password for lots / all of your online accounts, there are a couple of options to reduce your risk exposure: 
1. Reset your password on all of your online accounts.
<br />
<br />
2. So you may not have the time for that... at a minimum it is advisable to reset the passwords for your most critical accounts. 
These are the ones that you really do not want to be compromised, i.e. banking, online retailers (you may have your credit card stored there), social media etc. 

While you're there, this is probably a good time to start thinking about using a Password Manager too. They enable you to be able to use different passwords everywhere and take away the burden of having to remember them. I personally use <a href="https://1password.com">1Password</a>, although there are many others too such as <a href="https://www.lastpass.com">LastPass</a> and <a href="https://keepass.info">KeePass</a>. I would personally recommend 1Password or LastPass; they will likely work across all of your devices and make password management easy.

If you already use unique passwords for every online service, then you have greatly reduced your risk exposure. You could potentially take advantage of another service called <a href="https://haveibeenpwned.com/Passwords">Pwned Passwords</a>, also written and maintained by <a href="https://twitter.com/troyhunt">@troyhunt</a>. This site is able to let you know which of your passwords appear in a breach; if your password shows as 'pwned', then you just need to change this password on the online service(s) where you use it as soon as possible. 

A couple of things to note about Pwned Passwords:
1. It is secure. It employs <a href="https://blog.cloudflare.com/validating-leaked-passwords-with-k-anonymity/">k-Anonymity</a> which prevents the full password/hash from needing to be sent over the internet (for the techies out there, the article linked is worth a read).
<br />
<br />
2. Password Managers such as <a href="https://1password.com">1Password</a> can do all of the hard work for you. In particular, 1Password has a feature called watchtower which uses the Pwned Passwords service to inform you automatically about which passwords you should change. 

<br />
<br />
<br />
*Questions? Fire away on Twitter - <a href="https://twitter.com/sj_tate">@sj_tate</a>!*


- - - 
[1] https://www.owasp.org/index.php/Credential_stuffing