[Changelog](https://freemius.com/changelog/) / Cart-related improvements

### Improved cart recovery heuristics

We have improved the heuristics responsible for recovering cart sessions when a customer uses Freemius Checkout. A cart session can be seen as an introduction between Freemius and the customer. After being “introduced”, Freemius remembers the customer’s information so that they don’t have to enter it again when resuming their purchase.

However, these sessions can be lost because of various reasons. Luckily, we have advanced recovery heuristics in case this happens.

In this update, we focused on enhancing the recovery of lost carts. This will hopefully ensure higher conversion rates for our partners across the network.

### Additional fixes

- We will no longer send a cart email campaign if the user paid for the same plan in the last 3 months. This helps avoid duplicate emails where the cart session was lost and not recovered. Please [read this](help-documentation-marketing-automation-cart-abandonment-recovery.md) to learn more about our Cart Abandonment Recovery mechanism.