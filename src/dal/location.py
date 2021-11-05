# This module provides data access layer abstraction.
#
# To be implemented by concrete data providers.

import abc
import typing


# Location in a 3d-space.
class Location(typing.NamedTuple):
    x: float
    y: float
    altitude: float


class LocationFilterSpec(typing.NamedTuple):
    region: typing.Optional[str] = None
    loc_type: typing.Literal["city", "village", "all"] = "all"


RoadTypes = typing.Literal["asphalt", "gravel", "dirt", "singletrack"]


class RoadFilterSpec(typing.NamedTuple):
    acceptable_road_types: typing.Union[typing.Literal["all"], typing.List[RoadTypes]]


class FetcherInterface(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def fetch_loc(self, filter: LocationFilterSpec) -> typing.Mapping[str, Location]:
        raise NotImplementedError

    @abc.abstractmethod
    async def fetch_loc_async(self, filter: LocationFilterSpec) -> typing.Mapping[str, Location]:
        raise NotImplementedError

    
    @abc.abstractmethod
    def fetch_roads(self, filter: RoadFilterSpec) -> typing.List[typing.Tuple[str, str]]:
        raise NotImplementedError

    
    @abc.abstractmethod
    async def fetch_roads_async(self, filter: RoadFilterSpec) -> typing.List[typing.Tuple[str, str]]:
        raise NotImplementedError
