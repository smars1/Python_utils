import matplotlib.pyplot as plt
import re


# Given data
ID_SEMAFORO_PARTI_ACUM = [30, 10, 10, 10, 10, 30, 30, 10, 10]
index = list(range(1, len(ID_SEMAFORO_PARTI_ACUM) + 1 ))

    # Create bar graph
plt.bar(index, ID_SEMAFORO_PARTI_ACUM, color=['red' if value == 30 else 'green' for value in ID_SEMAFORO_PARTI_ACUM])
plt.xlabel('SEMANAS')
plt.ylabel('VALUE')
plt.title('ID_SEMAFORO_PARTICIPACION_SEMANAL Data Visualization')
plt.xticks(index)

    # Show the plot
plt.show()

def Participacion_Acum(data):
    """Generate a bar graph for the given data."""
    
    # Determine color for each bar based on its value
    colors = ['red' if value == 30 else 'orange' for value in data]
    
    # Create bar graph
    plt.bar(range(1, len(data) + 1), data, color=colors)
    plt.xlabel('SEMANAS')
    plt.ylabel('VALUE')
    plt.title('ID_SEMAFORO_PARTI_ACUM Data Visualization')
    plt.xticks(range(1, len(data) + 1))

    # Show the plot
    plt.show()

# Test the function
data = [30, 30, 30, 30, 30, 30, 30, 30, 30]
Participacion_Acum(data)







