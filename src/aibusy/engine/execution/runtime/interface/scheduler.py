from abc import ABC, abstractmethod


class Scheduler(
    ABC
):

    @abstractmethod
    def set_steps(
        self,
        steps: int,
    ):
        ...

    @property
    @abstractmethod
    def timesteps(
        self,
    ):
        ...

    @abstractmethod
    def scale_latents(
        self,
        latents,
        timestep,
    ):
        ...

    @abstractmethod
    def step(
        self,
        *,
        latents,
        noise,
        timestep,
    ):
        ...