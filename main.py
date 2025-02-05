
import subprocess

def run_all():
    print("Starting the training process...")
    subprocess.run(["python", "train_model.py"])  # Run training script

    print("Training completed. Running the test process...")
    subprocess.run(["python", "test_model.py"])  # Run testing script

    print("Testing completed. Running the prediction process...")
    subprocess.run(["python", "predict.py"])  # Run prediction script

    print("Process completed successfully!")

if __name__ == "__main__":
    run_all()
