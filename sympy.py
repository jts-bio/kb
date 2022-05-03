# %%
import sympy as sp

# %%
lam , sig , x = sp.symbols("lambda sigma x")

SYMBOLS = {
   "lam" : lam, 
   "sig": sig 
}

eq = sp.sympify("lam - 2 * sig",locals=SYMBOLS)
eq

# %%
def eqSym (left,right,symb_dict=SYMBOLS):
   return sp.Eq (sp.sympify(left,locals=symb_dict),sp.sympify (right,locals=symb_dict))

# %%
EQ = eqSym ("3 * x^2 + lam", "3 * sig")
EQ

# %%
EQ.subs({sig:45})
ANS = sp.solve(EQ,x)
for x in ANS:
   display(x)

# %%



