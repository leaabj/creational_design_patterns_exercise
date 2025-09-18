
from abc import ABC, abstractmethod
from uuid import uuid4
from .budget import GlobalBudget
from .campaign import Campaign


class ChannelClient(ABC):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def create_campaign(self, campaign: Campaign) -> str:
        pass

    @abstractmethod
    def pause_campaign(self, campaign_id: str) -> None:
        pass


class GoogleAdsClient(ChannelClient):
    def create_campaign(self, campaign: Campaign) -> str:
        budget = GlobalBudget()
        budget.allocate(campaign.daily_budget)
        external_id = f"g-{uuid4().hex[:8]}"
        return external_id

    def pause_campaign(self, campaign_id: str) -> None:
        pass

class FacebookAdsClient(ChannelClient):
    def create_campaign(self, campaign: Campaign) -> str:
        budget = GlobalBudget()
        budget.allocate(campaign.daily_budget)
        external_id = f"f-{uuid4().hex[:8]}"
        return external_id

    def pause_campaign(self, campaign_id: str) -> None:
        pass

class ChannelClientFactory:
    @staticmethod
    def create(channel: str) -> ChannelClient:
        if channel == "google":
            return GoogleAdsClient("google")
        elif channel == "facebook":
            return FacebookAdsClient("facebook")
        else:
            raise ValueError(f"Unknown channel: {channel}")
