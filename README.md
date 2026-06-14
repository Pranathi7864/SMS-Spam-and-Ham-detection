Stage 2: The XGBoost Brain (The "Judge")
Now that we have the numbers, we pass them to XGBoost.

What is it? XGBoost is a "Decision Tree" model. Imagine a massive game of "20 Questions."

How it works: The model asks questions based on the patterns it learned during train_model.py.



The Forest: XGBoost doesn't just use one tree; it uses hundreds of them. Each tree "votes," and the model combines those votes to get a final Probability (e.g., 98% Spam).

🔴 Stage 3: The Hybrid Result (The "Safety Switch")
This is the part we fixed earlier to make it Production Ready.

The AI's Vote: The XGBoost model gives its opinion (e.g., "I think this is Ham").

The Heuristic Override: Your code checks if any "Hard" red flags were found (like a .cc link).

Final Decision: If the AI says it's Spam OR the Heuristics see a dangerous link, the app shows the Red SPAM DETECTED box.
[19:51, 13/2/2026] Pranathi: Money in minutes!
Get collateral-free loans starting Rs 5000 through Vi Finance.
Fast-track your dreams with instant approval Click : viapp.onelink.me/bSC3/pl1
Sorry, I can't talk now.
 Dear Customer,
To enjoy seamless Banking use Digital Channels like Mobile, Internet Banking &ATM. Download Now: https://onelink.to/canarabankai1pe -Canara Bank
Master GenAI, ML, NLP & more with an 11-month program by IHFC, TIH of IIT Delhi. Next cohort filling up fast. https://simplimsg.com/SIMPLI/41Hhot
Simplilearn
ARRIVING EARLY: New Year Offers! Upto 10% off on Amazon, Flipkart, Westside & 40+ brand vouchers on Vi Shop. Save now https://viapp.onelink.me/bSC3/vshpoff