from ultralytics import YOLO

# Load YOLOv8 small model (faster and more accurate than nano)
model = YOLO("yolov8s.pt")

# Experiment folder name
experiment_name = "yolo_experiment_v2_T4"

# Train with optimized settings
model.train(
    data="/content/data.yaml",                           # Dataset config
    epochs=50,                                           # Training epochs
    imgsz=640,                                           # Image size
    batch=16,                                           # Batch size
    project="/content/drive/MyDrive/SpaceStationSafety", # Parent folder
    name=experiment_name,                                # Experiment name
    exist_ok=False,                                      # Don’t overwrite existing folder
    workers=2,                                           # Number of workers
    optimizer="SGD",                                     # Optimizer
    patience=20,                                         # Early stopping patience
    augment=True                                        # Use augmentations
)

print(f"✅ Training complete! Results saved in /content/drive/MyDrive/SpaceStationSafety/{experiment_name}")
