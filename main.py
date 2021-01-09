from bokeh.plotting import figure, output_file, show
import random

# Array of coordinates (x,y)
x_values = []
y_values = []

# Main function of Random Walks
def main(steps, reps):    
    path = []
    distances = []
    def random_walks(steps):
        x = 0
        y = 0
        for i in range (steps):
            step = random.choice(['UP','DOWN','LEFT','RIGHT'])
            if step == 'UP':
                y += 1
            elif step == 'DOWN':
                y -= 1
            elif step == 'LEFT':
                x -= 1
            else: 
                x += 1
            
        return (x,y)

    # Loop of n repetitions and n steps
    for i in range(reps):
        walk = random_walks(steps)
        print(walk, "Distance from home = ", abs(walk[0]) + abs(walk[1]))
        distance = abs(walk[0]) + abs(walk[1])
        distances.append(distance)
        x_values.append(walk[0])
        y_values.append(walk[1])
        path.append(walk)

    min_distance = min(distances)
    max_distance = max(distances)

    distances_length = len(distances)
    distances_sum = 0
    for i in distances:
        distances_sum += i
    
    avg_distance = int(distances_sum / distances_length)

    print(path)
    print(f'Minimun distance: {min_distance}')
    print(f'Maximun distance: {max_distance}')
    print(f'average distance: {avg_distance}')

    return x_values,y_values


    

if __name__ == "__main__":
    number_steps = int(input('How many steps do you want to walk: '))
    number_reps = int(input('How many reps do you want to do: '))
    main(number_steps, number_reps)
    output_file('simple__graphic.html')
    figure = figure()
    figure.line(x_values, y_values, line_width=2)
    show(figure)


