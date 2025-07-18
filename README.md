## #1 Initial Exploration: Cybersecurity

I am currently exploring different areas within computer engineering to decide my specialization.  
As a first step, I started with cybersecurity. 

I plan to continue improving this project until I finalize my decision about this area.  
Some of the upcoming enhancements include:

- Adding a password suggestion feature  (✓)
- Integrating online APIs to check for password breaches  
- Developing a graphical user interface (GUI)  
- Expanding the common password lists and improving performance  
- Exploring and integrating other cybersecurity tools and projects

---

# 🔐 Password Analyzer

This project is a small introduction to cybersecurity.  
It evaluates password strength based on the following criteria:

- Length  
- Use of uppercase and lowercase letters  
- Inclusion of digits  
- Presence of special characters  
- Whether the password appears in the top 10,000 most common passwords list  

The overall strength is calculated via a scoring system and explained to the user.

---

## Scoring System

| Criteria                      | Points    |
|------------------------------|-----------|
| Length (8 or more characters) | +3        |
| Uppercase letter             | +1        |
| Lowercase letter             | +1        |
| Digit                       | +1        |
| Special character           | +1        |

### Strength Levels

- 0-4 points: Weak Security  
- 5-6 points: Medium Security  
- 7 points: Strong Security  

If the password is found in the top 10,000 common passwords list, it is always considered **Very Weak**.

---

## 🛠️Update #1 - Password Suggestion Feature

I have implemented a new feature that automatically suggests improved versions of weak passwords.  
If the entered password lacks uppercase letters, digits, or special characters, the program adds these randomly to make it stronger.  
For example, if you enter `berkay123`, the program might suggest `berkay12B=3` or `berka|y12W3`.  
This feature aims to help users easily enhance their password security without changing their original password too much.

---

### Example Output
<pre> 
Enter a password to check: ılovecoding

--- Password Check Report ---

Password length is sufficient (✓)
Missing an uppercase letter (✗)
Contains a lowercase letter (✓)
Missing a digit (✗)
Missing a special character (✗)

Password Strength: Weak Security

--- Auto-fixed Suggestions ---
Fixed Password 1: ıloC/vecodin6g
Fixed Password 2: ılJov4ec)oding
Fixed Password 3: ıloveco6Gd{ing

Rechecking Fixed Passwords...

--- Password Check Report ---

Password length is sufficient (✓)
Contains an uppercase letter (✓)
Contains a lowercase letter (✓)
Contains a digit (✓)
Contains a special character (✓)

New Passwords Strength: Strong Security
</pre>
---

## Resources Used

- Top 10k common passwords list: [danielmiessler/SecLists](https://github.com/danielmiessler/SecLists)

---


