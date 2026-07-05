from abc import ABC, abstractmethod


class HuggingFaceClient(
    ABC
):

    @abstractmethod
    async def download_snapshot(
        self,
        *,
        repository: str,
        revision: str | None = None,
    ) -> str:
        """
        Download a repository snapshot and return the
        local directory where it has been installed.
        """
        ...