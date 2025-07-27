def suggest_food(mood, time, budget):
    if "hungry" in mood and budget <= 30:
        return "Grab a samosa and chai – college classic!"
    elif "sleepy" in mood:
        return "Cold coffee will wake you up. Or just nap in the library 😴"
    elif "bored" in mood:
        return "Spice it up with schezwan maggi or masala fries!"
    elif "excited" in mood and budget >= 50:
        return "Perfect day for chhole bhature or paneer roll!"
    elif "tired" in mood:
        return "Go light with poha or idli if it's morning. Maggi always works too."
    elif budget < 20:
        return "Not much today... Try butter toast or just water and manifest money 😅"
    elif "depressed" in mood or "sad" in mood:
        return "Treat yourself to chocolate pastry or french fries. You deserve it!"
    else:
        return "Can't decide? Go with the safest option: vada pav."

