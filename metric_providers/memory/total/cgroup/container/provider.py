import os

#pylint: disable=import-error
from metric_providers.base import BaseMetricProvider

class MemoryTotalCgroupContainerProvider(BaseMetricProvider):
    def __init__(self, resolution):
        super().__init__(
            metric_name="memory_total_cgroup_container",
            metrics={'time': int, 'value': int, 'container_id': str},
            resolution=resolution,
            unit="Bytes",
            current_dir=os.path.dirname(os.path.abspath(__file__)),
        )