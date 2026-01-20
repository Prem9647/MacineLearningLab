# Candidate Elimination Algorithm Implementation

# Step 1: Define training data
# Attributes: Role, Experience, Performance, Internet, Location
# Target: Approval (Yes / No)

training_data = [
    (["Technical", "Senior", "Excellent", "Good", "Urban"], "Yes"),
    (["Technical", "Junior", "Excellent", "Good", "Urban"], "Yes"),
    (["Non-Technical", "Junior", "Average", "Poor", "Rural"], "No"),
    (["Technical", "Senior", "Average", "Good", "Rural"], "No"),
    (["Technical", "Senior", "Excellent", "Good", "Rural"], "Yes")
]

num_attributes = len(training_data[0][0])

# Step 2: Initialize S and G
S = ["Ø"] * num_attributes          # Most specific hypothesis
G = [["?"] * num_attributes]        # Most general hypothesis


# Function to check consistency
def is_consistent(hypothesis, example):
    for h, e in zip(hypothesis, example):
        if h != "?" and h != e:
            return False
    return True


# Step 3: Process each training example
for instance, label in training_data:

    if label == "Yes":  # Positive example
        # Remove inconsistent hypotheses from G
        G = [g for g in G if is_consistent(g, instance)]

        # Generalize S
        for i in range(num_attributes):
            if S[i] == "Ø":
                S[i] = instance[i]
            elif S[i] != instance[i]:
                S[i] = "?"

    else:  # Negative example
        new_G = []
        for g in G:
            if is_consistent(g, instance):
                for i in range(num_attributes):
                    if g[i] == "?":
                        if S[i] != "?" and S[i] != "Ø":
                            new_hypothesis = g.copy()
                            new_hypothesis[i] = S[i]
                            new_G.append(new_hypothesis)
            else:
                new_G.append(g)
        G = new_G

    print("Current S:", S)
    print("Current G:", G)
    print("-" * 50)


# Step 4: Final boundaries
print("Final Specific Hypothesis (S):", S)
print("Final General Hypotheses (G):", G)