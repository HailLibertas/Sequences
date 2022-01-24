flowers = [
    "Daffodil",
    "Evening Primrose",
    "Hydrangea",
    "Iris",
    "Lavender",
    "Sunflower",
    "Tiger Lily",

]
# for flower in flowers:
#     print(flower)
separator = ", "
output = separator.join(flowers)
print(output)

print(", ".join(flowers))

# Join method witch is a str menthod etirates lists for us instead of
# using a for loop