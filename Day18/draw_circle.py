import turtle as t

t.speed("fastest")

for _ in range(200):
    t.circle(100)
    t.left(2)

for _ in range(200):
    t.circle(100)
    t.setheading(t.heading() + 2)

# Without Overlap
for _ in range(360 // 5):
    t.circle(100)
    t.setheading(t.heading() + 5)
