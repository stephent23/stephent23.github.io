---
type: posts
title: How Are the Three Digits on the Back of Your Credit Card Computed?
tags: [Cryptography, Online Shopping, CNP, Credit Card, Money, Security, DES, CVV, Debit Card]
category: Cryptography
classes: wide
---

The three digits that are printed on the back of a credit or debit card are computed by an algorithm which uses the 2-key Triple DES (Data Encryption Standard) encryption algorithm. In order to produce the three digits, several inputs to the algorithm are required:

<ol>
    <li>Primary Account Number (PAN)</li>
    <ul>
        <li>This is the long account number on the front of the card.</li>
    </ul>
    <li>Card Expiration Date</li>
    <br />
    <li>Service Code</li>
    <ul>
        <li>This is a three-digit code where each number specifies; interchange rules, the authorisation processing that is required, and the range of services that are permitted.</li>
    </ul>
    <li>2 DES encryption keys</li>
    <ul>
        <li>These are known only to the card issuer.</li>
    </ul>
</ol>

The 2-key Triple DES algorithm (2TDES) is what provides security to the CVV number. Providing that the card issuer keeps the 2 DES keys secret, it is believed that it is not possible for anyone else to be able to calculate the CVV code. Triple DES works by repeating the standard DES algorithm three times; encrypting the data with the first key, decrypting with the second key and then finally encrypting with the first key again. This is able to be written as: 
<br />
<br />

\begin{aligned} 
    \text{CVV} & = E_{\text{K1}} ( D_{\text{K2}} (E_{\text{K1}} (PAN||Expiry Date||Service Code))) 
\end{aligned}
{: .align-center}


![CVV generation process](/assets/img/custom/posts/CVV_generation_process.png)

This three-digit output is then embossed onto the back of the card and is what is known as the CVV (CVV_2) number. Subsequently, when a cardholder makes a card not present (CNP) payment, for example on the internet, they are asked to provide the PAN, expiration date and the CVV number. The card issuer will then use the inputs to compute the CVV algorithm again. It will then compare the output from the algorithm to the CVV number that was input by the card holder. If they match, the payment will be authorised.

![CVV verification process](/assets/img/custom/posts/CVV_verification_process.png){: .align-center}

<br />