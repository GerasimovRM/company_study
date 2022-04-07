# Привет как дела
# П-Р-И-В-Е-Т К-А-К Д-Е-Л-А

st = input().upper()
lst = st.split()
lst2 = ["-".join(list(word)) for word in lst]
print(" ".join(lst2))
