"""
Driver script - PoC
"""

import requests

from config import PYSPARK_API_URL, logger


def main():
    print("\nPoC - Validation\n")
    employee_data = {
        "id": [f"E{(idx):03}" for idx in range(1, 5)],
        "name": ["Max", "Joachim", "Eric", "Adolf"],
        "badge": ["KC2", "KC1", "KC2", "KC1"],
        "score": [100, 120, 90, 105],
    }

    try:
        health_check = requests.get(f"{PYSPARK_API_URL}/health")
        hc_response = health_check.json()

        logger.info(f"Health check - {hc_response}")

        response = requests.post(
            f"{PYSPARK_API_URL}/agg", json={"employee_data": employee_data}
        )
        agg_response = response.json()

        logger.info(f"{agg_response}")
    except Exception as e:
        print(f"ERROR : {e}")
        exit(-1)


if __name__ == "__main__":
    main()
