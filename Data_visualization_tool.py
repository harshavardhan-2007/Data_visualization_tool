import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

def load_data(file_path):
    try:
        df = pd.read_csv(file_path)
        print("✅ Data loaded successfully!\n")
        print(df.head())
        return df
    except Exception as e:
        print("❌ Error loading file:", e)
        return None


def plot_matplotlib(df):
    print("\n📊 Matplotlib Plot")
    x = input("Enter X column: ")
    y = input("Enter Y column: ")

    plt.figure()
    plt.plot(df[x], df[y])
    plt.xlabel(x)
    plt.ylabel(y)
    plt.title(f"{x} vs {y}")
    plt.show()


def plot_seaborn(df):
    print("\n📊 Seaborn Plot")
    x = input("Enter X column: ")
    y = input("Enter Y column: ")

    sns.scatterplot(data=df, x=x, y=y)
    plt.title(f"{x} vs {y}")
    plt.show()


def plot_plotly(df):
    print("\n📊 Plotly Interactive Plot")
    x = input("Enter X column: ")
    y = input("Enter Y column: ")

    fig = px.scatter(df, x=x, y=y, title=f"{x} vs {y}")
    fig.show()


def main():
    file_path = input("Enter CSV file path: ")
    df = load_data(file_path)

    if df is None:
        return

    while True:
        print("\nChoose Visualization:")
        print("1. Matplotlib (Line)")
        print("2. Seaborn (Scatter)")
        print("3. Plotly (Interactive)")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            plot_matplotlib(df)
        elif choice == "2":
            plot_seaborn(df)
        elif choice == "3":
            plot_plotly(df)
        elif choice == "4":
            print("👋 Exiting...")
            break
        else:
            print("❌ Invalid choice")


if __name__ == "__main__":
    main()