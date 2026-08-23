# coding: utf-8

# flake8: noqa

"""
    Gnaww Developer API

    Reviewed public print-intelligence contract for direct HTTP, CLI, SDK and MCP consumers. Capability fit is not price, live availability, producer acceptance or an order.

    The version of the OpenAPI document: 0.1

"""  # noqa: E501


__version__ = "0.1.0"

# Define package exports
__all__ = [
    "ProducerCapabilitiesApi",
    "RecipesApi",
    "SpecMatchApi",
    "HealthApi",
    "InterpretationApi",
    "TransformApi",
    "ApiResponse",
    "ApiClient",
    "Configuration",
    "OpenApiException",
    "ApiTypeError",
    "ApiValueError",
    "ApiKeyError",
    "ApiAttributeError",
    "ApiException",
    "ApparelDecorationOptions",
    "ApparelOptions",
    "ArtworkRequirements",
    "AvailabilityCapability",
    "BenchmarkQuantityGuidance",
    "BookDocumentOptions",
    "CapabilityEvidence",
    "ColourCapability",
    "CommercialPrintOptions",
    "ContinuePrintRequirementInterpretationDefaultResponse",
    "ContinuePrintRequirementInterpretationDefaultResponseError",
    "ContinuePrintRequirementRequest",
    "ContinuePrintRequirementResponse",
    "ControlledInterpretationState",
    "CustomDimensionCapability",
    "DecorationAreaCapability",
    "DeliveryDestination",
    "DimensionCapability",
    "FabricHomewaresCapabilityOptions",
    "FabricHomewaresOptions",
    "FinishedSize",
    "Finishing",
    "FoldedLeafletOptions",
    "FulfilmentMatchResult",
    "FulfilmentRequirement",
    "Gjs",
    "Gjs1",
    "GrammageRequirement",
    "GroundedProductMeaning",
    "HealthResponse",
    "IntentClassificationResponse",
    "IntentPlanEvidence",
    "IntentProviderMetadata",
    "InterpretPrintRequirementDefaultResponse",
    "InterpretPrintRequirementDefaultResponseError",
    "InterpretPrintRequirementRequest",
    "InterpretPrintRequirementResponse",
    "Issue",
    "IssueSet",
    "MatchDifference",
    "MatchPrintDemandDefaultResponse",
    "MatchPrintDemandRequest",
    "MatchPrintDemandResponse",
    "MatchPrintDemandUniverseRequest",
    "MatchPrintDemandUniverseResponse",
    "MatchRecipeRequest",
    "MatchRecipeResponse",
    "MaterialCapability",
    "MaterialCompositionPart",
    "PersonalisationCapability",
    "PhysicalRequirementDecision",
    "PrintComponent",
    "PrintJobSpecification",
    "PrintJobSpecificationV04",
    "PrintSpec",
    "ProducerBookDocumentOptions",
    "ProducerCapabilityResource",
    "ProducerComponentCapability",
    "ProducerFinishingCapability",
    "ProducerFoldedLeafletOptions",
    "ProducerProcessCapability",
    "ProducerProductCapability",
    "ProducerProductOptionCapability",
    "ProducerProductReference",
    "ProductMeaningDecisionPoint",
    "ProductMeaningFamilyContext",
    "ProductOptions",
    "ProductPackBenchmarkReference",
    "ProductPackClarification",
    "ProductPackRecommendation",
    "ProductPackResponse",
    "PromotionalGoodsCapabilityOptions",
    "PromotionalGoodsOptions",
    "PublicClarificationAnswer",
    "PublicClarificationOption",
    "PublicClarificationQuestion",
    "PublicFulfilmentState",
    "PublicMatchTargetRequest",
    "PublicMatchTargetState",
    "PublicProducerUniverseCandidate",
    "PublicRecipeState",
    "PublicSpecMatchReadiness",
    "PublicUseConditionReview",
    "Quantity",
    "QuantityRange",
    "RecipeResource",
    "RepeatPatternCapability",
    "ResolveRecipeRequest",
    "ResolveRecipeResponse",
    "ResolvedRecipeMatchState",
    "ServiceRequirements",
    "SourceInput",
    "SpecMatchResult",
    "Substrate",
    "TransformRequest",
    "TransformResponse",
    "TurnaroundCapability",
    "UseRequirement",
    "WashabilityCapability",
]

# import apis into sdk package
from gnaww_sdk.api.producer_capabilities_api import ProducerCapabilitiesApi as ProducerCapabilitiesApi
from gnaww_sdk.api.recipes_api import RecipesApi as RecipesApi
from gnaww_sdk.api.spec_match_api import SpecMatchApi as SpecMatchApi
from gnaww_sdk.api.health_api import HealthApi as HealthApi
from gnaww_sdk.api.interpretation_api import InterpretationApi as InterpretationApi
from gnaww_sdk.api.transform_api import TransformApi as TransformApi

# import ApiClient
from gnaww_sdk.api_response import ApiResponse as ApiResponse
from gnaww_sdk.api_client import ApiClient as ApiClient
from gnaww_sdk.configuration import Configuration as Configuration
from gnaww_sdk.exceptions import OpenApiException as OpenApiException
from gnaww_sdk.exceptions import ApiTypeError as ApiTypeError
from gnaww_sdk.exceptions import ApiValueError as ApiValueError
from gnaww_sdk.exceptions import ApiKeyError as ApiKeyError
from gnaww_sdk.exceptions import ApiAttributeError as ApiAttributeError
from gnaww_sdk.exceptions import ApiException as ApiException

# import models into sdk package
from gnaww_sdk.models.apparel_decoration_options import ApparelDecorationOptions as ApparelDecorationOptions
from gnaww_sdk.models.apparel_options import ApparelOptions as ApparelOptions
from gnaww_sdk.models.artwork_requirements import ArtworkRequirements as ArtworkRequirements
from gnaww_sdk.models.availability_capability import AvailabilityCapability as AvailabilityCapability
from gnaww_sdk.models.benchmark_quantity_guidance import BenchmarkQuantityGuidance as BenchmarkQuantityGuidance
from gnaww_sdk.models.book_document_options import BookDocumentOptions as BookDocumentOptions
from gnaww_sdk.models.capability_evidence import CapabilityEvidence as CapabilityEvidence
from gnaww_sdk.models.colour_capability import ColourCapability as ColourCapability
from gnaww_sdk.models.commercial_print_options import CommercialPrintOptions as CommercialPrintOptions
from gnaww_sdk.models.continue_print_requirement_interpretation_default_response import ContinuePrintRequirementInterpretationDefaultResponse as ContinuePrintRequirementInterpretationDefaultResponse
from gnaww_sdk.models.continue_print_requirement_interpretation_default_response_error import ContinuePrintRequirementInterpretationDefaultResponseError as ContinuePrintRequirementInterpretationDefaultResponseError
from gnaww_sdk.models.continue_print_requirement_request import ContinuePrintRequirementRequest as ContinuePrintRequirementRequest
from gnaww_sdk.models.continue_print_requirement_response import ContinuePrintRequirementResponse as ContinuePrintRequirementResponse
from gnaww_sdk.models.controlled_interpretation_state import ControlledInterpretationState as ControlledInterpretationState
from gnaww_sdk.models.custom_dimension_capability import CustomDimensionCapability as CustomDimensionCapability
from gnaww_sdk.models.decoration_area_capability import DecorationAreaCapability as DecorationAreaCapability
from gnaww_sdk.models.delivery_destination import DeliveryDestination as DeliveryDestination
from gnaww_sdk.models.dimension_capability import DimensionCapability as DimensionCapability
from gnaww_sdk.models.fabric_homewares_capability_options import FabricHomewaresCapabilityOptions as FabricHomewaresCapabilityOptions
from gnaww_sdk.models.fabric_homewares_options import FabricHomewaresOptions as FabricHomewaresOptions
from gnaww_sdk.models.finished_size import FinishedSize as FinishedSize
from gnaww_sdk.models.finishing import Finishing as Finishing
from gnaww_sdk.models.folded_leaflet_options import FoldedLeafletOptions as FoldedLeafletOptions
from gnaww_sdk.models.fulfilment_match_result import FulfilmentMatchResult as FulfilmentMatchResult
from gnaww_sdk.models.fulfilment_requirement import FulfilmentRequirement as FulfilmentRequirement
from gnaww_sdk.models.gjs import Gjs as Gjs
from gnaww_sdk.models.gjs1 import Gjs1 as Gjs1
from gnaww_sdk.models.grammage_requirement import GrammageRequirement as GrammageRequirement
from gnaww_sdk.models.grounded_product_meaning import GroundedProductMeaning as GroundedProductMeaning
from gnaww_sdk.models.health_response import HealthResponse as HealthResponse
from gnaww_sdk.models.intent_classification_response import IntentClassificationResponse as IntentClassificationResponse
from gnaww_sdk.models.intent_plan_evidence import IntentPlanEvidence as IntentPlanEvidence
from gnaww_sdk.models.intent_provider_metadata import IntentProviderMetadata as IntentProviderMetadata
from gnaww_sdk.models.interpret_print_requirement_default_response import InterpretPrintRequirementDefaultResponse as InterpretPrintRequirementDefaultResponse
from gnaww_sdk.models.interpret_print_requirement_default_response_error import InterpretPrintRequirementDefaultResponseError as InterpretPrintRequirementDefaultResponseError
from gnaww_sdk.models.interpret_print_requirement_request import InterpretPrintRequirementRequest as InterpretPrintRequirementRequest
from gnaww_sdk.models.interpret_print_requirement_response import InterpretPrintRequirementResponse as InterpretPrintRequirementResponse
from gnaww_sdk.models.issue import Issue as Issue
from gnaww_sdk.models.issue_set import IssueSet as IssueSet
from gnaww_sdk.models.match_difference import MatchDifference as MatchDifference
from gnaww_sdk.models.match_print_demand_default_response import MatchPrintDemandDefaultResponse as MatchPrintDemandDefaultResponse
from gnaww_sdk.models.match_print_demand_request import MatchPrintDemandRequest as MatchPrintDemandRequest
from gnaww_sdk.models.match_print_demand_response import MatchPrintDemandResponse as MatchPrintDemandResponse
from gnaww_sdk.models.match_print_demand_universe_request import MatchPrintDemandUniverseRequest as MatchPrintDemandUniverseRequest
from gnaww_sdk.models.match_print_demand_universe_response import MatchPrintDemandUniverseResponse as MatchPrintDemandUniverseResponse
from gnaww_sdk.models.match_recipe_request import MatchRecipeRequest as MatchRecipeRequest
from gnaww_sdk.models.match_recipe_response import MatchRecipeResponse as MatchRecipeResponse
from gnaww_sdk.models.material_capability import MaterialCapability as MaterialCapability
from gnaww_sdk.models.material_composition_part import MaterialCompositionPart as MaterialCompositionPart
from gnaww_sdk.models.personalisation_capability import PersonalisationCapability as PersonalisationCapability
from gnaww_sdk.models.physical_requirement_decision import PhysicalRequirementDecision as PhysicalRequirementDecision
from gnaww_sdk.models.print_component import PrintComponent as PrintComponent
from gnaww_sdk.models.print_job_specification import PrintJobSpecification as PrintJobSpecification
from gnaww_sdk.models.print_job_specification_v04 import PrintJobSpecificationV04 as PrintJobSpecificationV04
from gnaww_sdk.models.print_spec import PrintSpec as PrintSpec
from gnaww_sdk.models.producer_book_document_options import ProducerBookDocumentOptions as ProducerBookDocumentOptions
from gnaww_sdk.models.producer_capability_resource import ProducerCapabilityResource as ProducerCapabilityResource
from gnaww_sdk.models.producer_component_capability import ProducerComponentCapability as ProducerComponentCapability
from gnaww_sdk.models.producer_finishing_capability import ProducerFinishingCapability as ProducerFinishingCapability
from gnaww_sdk.models.producer_folded_leaflet_options import ProducerFoldedLeafletOptions as ProducerFoldedLeafletOptions
from gnaww_sdk.models.producer_process_capability import ProducerProcessCapability as ProducerProcessCapability
from gnaww_sdk.models.producer_product_capability import ProducerProductCapability as ProducerProductCapability
from gnaww_sdk.models.producer_product_option_capability import ProducerProductOptionCapability as ProducerProductOptionCapability
from gnaww_sdk.models.producer_product_reference import ProducerProductReference as ProducerProductReference
from gnaww_sdk.models.product_meaning_decision_point import ProductMeaningDecisionPoint as ProductMeaningDecisionPoint
from gnaww_sdk.models.product_meaning_family_context import ProductMeaningFamilyContext as ProductMeaningFamilyContext
from gnaww_sdk.models.product_options import ProductOptions as ProductOptions
from gnaww_sdk.models.product_pack_benchmark_reference import ProductPackBenchmarkReference as ProductPackBenchmarkReference
from gnaww_sdk.models.product_pack_clarification import ProductPackClarification as ProductPackClarification
from gnaww_sdk.models.product_pack_recommendation import ProductPackRecommendation as ProductPackRecommendation
from gnaww_sdk.models.product_pack_response import ProductPackResponse as ProductPackResponse
from gnaww_sdk.models.promotional_goods_capability_options import PromotionalGoodsCapabilityOptions as PromotionalGoodsCapabilityOptions
from gnaww_sdk.models.promotional_goods_options import PromotionalGoodsOptions as PromotionalGoodsOptions
from gnaww_sdk.models.public_clarification_answer import PublicClarificationAnswer as PublicClarificationAnswer
from gnaww_sdk.models.public_clarification_option import PublicClarificationOption as PublicClarificationOption
from gnaww_sdk.models.public_clarification_question import PublicClarificationQuestion as PublicClarificationQuestion
from gnaww_sdk.models.public_fulfilment_state import PublicFulfilmentState as PublicFulfilmentState
from gnaww_sdk.models.public_match_target_request import PublicMatchTargetRequest as PublicMatchTargetRequest
from gnaww_sdk.models.public_match_target_state import PublicMatchTargetState as PublicMatchTargetState
from gnaww_sdk.models.public_producer_universe_candidate import PublicProducerUniverseCandidate as PublicProducerUniverseCandidate
from gnaww_sdk.models.public_recipe_state import PublicRecipeState as PublicRecipeState
from gnaww_sdk.models.public_spec_match_readiness import PublicSpecMatchReadiness as PublicSpecMatchReadiness
from gnaww_sdk.models.public_use_condition_review import PublicUseConditionReview as PublicUseConditionReview
from gnaww_sdk.models.quantity import Quantity as Quantity
from gnaww_sdk.models.quantity_range import QuantityRange as QuantityRange
from gnaww_sdk.models.recipe_resource import RecipeResource as RecipeResource
from gnaww_sdk.models.repeat_pattern_capability import RepeatPatternCapability as RepeatPatternCapability
from gnaww_sdk.models.resolve_recipe_request import ResolveRecipeRequest as ResolveRecipeRequest
from gnaww_sdk.models.resolve_recipe_response import ResolveRecipeResponse as ResolveRecipeResponse
from gnaww_sdk.models.resolved_recipe_match_state import ResolvedRecipeMatchState as ResolvedRecipeMatchState
from gnaww_sdk.models.service_requirements import ServiceRequirements as ServiceRequirements
from gnaww_sdk.models.source_input import SourceInput as SourceInput
from gnaww_sdk.models.spec_match_result import SpecMatchResult as SpecMatchResult
from gnaww_sdk.models.substrate import Substrate as Substrate
from gnaww_sdk.models.transform_request import TransformRequest as TransformRequest
from gnaww_sdk.models.transform_response import TransformResponse as TransformResponse
from gnaww_sdk.models.turnaround_capability import TurnaroundCapability as TurnaroundCapability
from gnaww_sdk.models.use_requirement import UseRequirement as UseRequirement
from gnaww_sdk.models.washability_capability import WashabilityCapability as WashabilityCapability
from gnaww_sdk.convenience import (
    GnawwApiError,
    GnawwClient,
    GnawwPublicError,
    GnawwResponse,
)
