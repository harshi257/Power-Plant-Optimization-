# src/power_plant_optimization/exception.py

class PowerPlantOptimizationError(Exception):
    """Base exception for all errors in the Power Plant Optimization package."""
    pass


class DataValidationError(PowerPlantOptimizationError):
    """Raised when input data fails validation checks."""

    def __init__(self, message="Data validation failed"):
        super().__init__(message)


class FeatureEngineeringError(PowerPlantOptimizationError):
    """Raised when feature engineering fails."""

    def __init__(self, message="Feature engineering failed"):
        super().__init__(message)


class ModelTrainingError(PowerPlantOptimizationError):
    """Raised when model training or optimization fails."""

    def __init__(self, message="Model training failed"):
        super().__init__(message)


class ModelPredictionError(PowerPlantOptimizationError):
    """Raised when model prediction fails."""

    def __init__(self, message="Model prediction failed"):
        super().__init__(message)
