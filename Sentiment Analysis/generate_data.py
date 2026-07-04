"""
generate_data.py
-----------------
Creates a small labeled dataset of customer product reviews
(reviews.csv) with positive, negative, and neutral sentiment labels.
All text below is original/synthetic, written for this project.
"""

import csv
import random

random.seed(3)

positive_templates = [
    "This product exceeded my expectations, {topic} is fantastic.",
    "I absolutely love the {topic}, works perfectly every time.",
    "Great value for money, {topic} quality is excellent.",
    "Fast delivery and the {topic} feels premium.",
    "Highly recommend this, the {topic} is exactly what I needed.",
    "Customer support was helpful and the {topic} works great.",
    "Really happy with this purchase, {topic} is outstanding.",
    "Five stars, the {topic} is durable and reliable.",
]

negative_templates = [
    "Very disappointed, the {topic} stopped working after a week.",
    "Poor quality, {topic} feels cheap and flimsy.",
    "I regret buying this, the {topic} does not work as advertised.",
    "Terrible experience, {topic} arrived damaged.",
    "Waste of money, the {topic} broke on the first use.",
    "Customer service was unhelpful about the {topic} issue.",
    "Not worth the price, {topic} quality is bad.",
    "Extremely frustrated, the {topic} is defective.",
]

neutral_templates = [
    "The {topic} is okay, nothing special but does the job.",
    "Average product, {topic} works as expected, no surprises.",
    "It's fine, the {topic} matches the description provided.",
    "Delivery took a while but the {topic} is acceptable.",
    "The {topic} is decent for the price, could be better.",
    "It works, though the {topic} design could be improved.",
]

topics = ["battery life", "build quality", "screen", "sound", "packaging",
          "shipping speed", "user interface", "material", "size", "performance",
          "camera", "connectivity", "design", "warranty support", "instructions"]

rows = []
review_id = 1
for _ in range(80):
    template = random.choice(positive_templates)
    rows.append([review_id, template.format(topic=random.choice(topics)), "positive"])
    review_id += 1

for _ in range(80):
    template = random.choice(negative_templates)
    rows.append([review_id, template.format(topic=random.choice(topics)), "negative"])
    review_id += 1

for _ in range(40):
    template = random.choice(neutral_templates)
    rows.append([review_id, template.format(topic=random.choice(topics)), "neutral"])
    review_id += 1

random.shuffle(rows)

with open("reviews.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["review_id", "review_text", "sentiment"])
    writer.writerows(rows)

print(f"Generated reviews.csv with {len(rows)} reviews "
      f"(80 positive, 80 negative, 40 neutral)")