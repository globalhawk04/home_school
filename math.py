import random
import webbrowser
import os

def generate_problems(count, difficulty):
    problems = []
    
    # Define ranges based on difficulty
    if difficulty == 'easy':
        num_min, num_max = 1, 10
        show_visuals = True
    elif difficulty == 'medium':
        num_min, num_max = 10, 100
        show_visuals = False
    else: # hard
        num_min, num_max = 100, 1000
        show_visuals = False

    operations = ['+', '-', '*', '/']

    for _ in range(count):
        op = random.choice(operations)
        
        # Basic generation
        num1 = random.randint(num_min, num_max)
        num2 = random.randint(num_min, num_max)

        # Apply Rules
        if op == '-':
            # Ensure answer is not negative
            if num1 < num2:
                num1, num2 = num2, num1
        
        elif op == '/':
            # Ensure answer is a whole number
            # Method: Generate the answer first, then multiply to get the large number
            answer = random.randint(num_min, num_max) 
            
            if difficulty == 'easy':
                num2 = random.randint(1, 5) 
                answer = random.randint(1, 10)
            else:
                num2 = random.randint(2, 12) 
                answer = random.randint(num_min, num_max)
            
            num1 = answer * num2
        
        # Visuals logic (only for Easy)
        visual_html = ""
        if show_visuals:
            # Helper to make dots
            def make_dots(n, color):
                # We add a specific border to ensure it prints even if color is off
                return f'<div class="dots-group">{"".join([f"<span class=dot style=background-color:{color}></span>" for _ in range(n)])}</div>'

            if op == '+':
                visual_html = f'<div class="visual">{make_dots(num1, "#888")} + {make_dots(num2, "#333")}</div>'
            elif op == '-':
                visual_html = f'<div class="visual">{make_dots(num1, "#888")} - {make_dots(num2, "#fff")}</div>'
            elif op == '*':
                if num1 * num2 <= 50: 
                    visual_html = '<div class="visual">'
                    for _ in range(num1):
                        visual_html += make_dots(num2, "#555") + " "
                    visual_html += '</div>'
            elif op == '/':
                if num1 <= 50:
                    visual_html = f'<div class="visual">Start with: {make_dots(num1, "#555")}</div>'

        # Format symbols for display
        display_op = '÷' if op == '/' else ('×' if op == '*' else op)

        problems.append({
            'n1': num1,
            'n2': num2,
            'op': display_op,
            'visual': visual_html
        })

    return problems

def create_html(problems, difficulty):
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Math Worksheet</title>
        <style>
            body {{ 
                font-family: 'Arial', sans-serif; 
                max-width: 850px; 
                margin: 0 auto; 
                padding: 40px; 
                color: #000;
            }}
            
            /* Header for Name and Date */
            .header {{
                display: flex;
                justify-content: space-between;
                margin-bottom: 40px;
                font-size: 1.2em;
                border-bottom: 2px solid #333;
                padding-bottom: 20px;
            }}
            
            h1 {{ 
                text-align: center; 
                font-size: 2em; 
                margin-bottom: 10px;
                text-transform: uppercase;
                letter-spacing: 2px;
            }}

            .problem-container {{
                display: flex;
                flex-wrap: wrap;
                justify-content: space-between;
            }}
            
            /* The Problem Card */
            .card {{
                border: 1px solid #000;
                border-radius: 8px;
                padding: 20px;
                margin-bottom: 20px;
                width: 45%; /* Two columns */
                box-sizing: border-box;
                page-break-inside: avoid; /* Prevent cutting problem in half */
            }}
            
            .equation {{
                font-size: 2.5em;
                font-weight: bold;
                text-align: center;
                margin-top: 10px;
                line-height: 1.5em;
            }}
            
            /* The writing line for the child */
            .answer-line {{
                display: inline-block;
                width: 100px;
                border-bottom: 3px solid #000;
                margin-left: 10px;
            }}

            /* Visual Styles */
            .visual {{ 
                text-align: center; 
                margin-bottom: 15px; 
                /* Force browsers to print background colors */
                -webkit-print-color-adjust: exact; 
                print-color-adjust: exact; 
            }}
            
            .dots-group {{ 
                display: inline-block; 
                margin: 2px; 
                padding: 2px; 
            }}
            
            .dot {{
                height: 15px;
                width: 15px;
                border-radius: 50%;
                display: inline-block;
                margin: 2px;
                border: 1px solid #000; /* Important for B&W printing */
            }}

            /* Print Controls */
            .controls {{ text-align: center; margin-bottom: 20px; }}
            @media print {{
                .controls {{ display: none; }}
                body {{ padding: 0; margin: 0; }}
                .card {{ box-shadow: none; }}
            }}
        </style>
    </head>
    <body>

        <div class="controls">
            <button onclick="window.print()" style="font-size: 20px; padding: 10px 20px; background: #333; color: white; border: none; cursor: pointer;">🖨️ Print Worksheet</button>
        </div>

        <div class="header">
            <div>Name: __________________________</div>
            <div>Date: __________________________</div>
        </div>

        <h1>{difficulty.capitalize()} Math</h1>
        
        <div class="problem-container">
    """

    for p in problems:
        html_content += f"""
            <div class="card">
                {p['visual']}
                <div class="equation">
                    {p['n1']} {p['op']} {p['n2']} = <span class="answer-line"></span>
                </div>
            </div>
        """

    html_content += """
        </div>
    </body>
    </html>
    """
    
    filename = "math_worksheet.html"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(html_content)
    
    return filename

def main():
    print("--- Worksheet Generator ---")
    
    # 1. Ask for Number of Problems
    while True:
        try:
            count = int(input("How many problems do you want? (e.g., 10): "))
            if count > 0: break
            print("Please enter a number greater than 0.")
        except ValueError:
            print("That's not a number! Try again.")

    # 2. Ask for Difficulty
    while True:
        diff = input("Difficulty (easy, medium, hard): ").lower().strip()
        if diff in ['easy', 'medium', 'hard']:
            break
        print("Please type 'easy', 'medium', or 'hard'.")

    # 3. Generate and Save
    problems = generate_problems(count, diff)
    file_path = create_html(problems, diff)
    
    print(f"\nSuccess! Generated {count} {diff} problems.")
    print(f"Opening {file_path} now...")
    
    # Automatically open the file in the browser
    webbrowser.open('file://' + os.path.realpath(file_path))

if __name__ == "__main__":
    main()
