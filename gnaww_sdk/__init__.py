# coding: utf-8

# flake8: noqa

"""
    Gnaww Developer API

    Reviewed public print-intelligence contract for direct HTTP, CLI, SDK and MCP consumers. Capability fit is not price, live availability, producer acceptance or an order.

    The version of the OpenAPI document: 0.1

"""  # noqa: E501


__version__ = "0.2.0"

# Define package exports
__all__ = [
    "ProducerCapabilitiesApi",
    "RecipesApi",
    "SpecMatchApi",
    "SpecificationsApi",
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
    "AppModelsManufacturingGeometryMaterialCompositionPart",
    "AppModelsProducerMaterialCompositionPart",
    "ApparelDecorationOptions",
    "ApparelOptions",
    "ArtworkRequirements",
    "AssemblyOperationParameters",
    "AvailabilityCapability",
    "BenchmarkQuantityGuidance",
    "BookDocumentOptions",
    "CapabilityEvidence",
    "Circle2D",
    "ColourCapability",
    "CommercialPrintOptions",
    "ContinueInterpretationRequestV02",
    "ContinuePrintRequirementInterpretationDefaultResponse",
    "ContinuePrintRequirementInterpretationDefaultResponseError",
    "Contour",
    "CreateSpecificationRequest",
    "CreateSpecificationResponse",
    "CustomDimensionCapability",
    "CutOperationParameters",
    "DecorationAreaCapability",
    "DecorationOperationParameters",
    "DeliveryDestination",
    "DimensionCapability",
    "DrillHole",
    "DrillOperationParameters",
    "EdgeRelativePoint",
    "FabricHomewaresCapabilityOptions",
    "FabricHomewaresOptions",
    "FinishedSize",
    "Finishing",
    "FoldLine",
    "FoldOperationParameters",
    "FoldPanel",
    "FoldedLeafletOptions",
    "FulfilmentMatchResult",
    "FulfilmentRequirement",
    "Gjs",
    "Gjs1",
    "GrammageRequirement",
    "GroundedProductMeaning",
    "HealthResponse",
    "InspectOperationParameters",
    "IntentClassificationResponse",
    "IntentPlanEvidence",
    "IntentProviderMetadata",
    "InterpretPrintRequirementDefaultResponse",
    "InterpretPrintRequirementDefaultResponseError",
    "InterpretPrintRequirementRequest",
    "InterpretationResultV02",
    "Issue",
    "IssueSet",
    "LegacyOperationParameters",
    "Line2D",
    "ManufacturingAssembly",
    "ManufacturingComponent",
    "ManufacturingGeometry",
    "ManufacturingMaterial",
    "ManufacturingOperation",
    "ManufacturingOperationParameters",
    "ManufacturingQuantity",
    "ManufacturingRegion",
    "ManufacturingRegionGeometry",
    "ManufacturingVariation",
    "MatchDifference",
    "MatchPrintDemandDefaultResponse",
    "MatchPrintDemandRequest",
    "MatchPrintDemandResponse",
    "MatchPrintDemandUniverseRequest",
    "MatchPrintDemandUniverseResponse",
    "MatchRecipeRequest",
    "MatchRecipeResponse",
    "MaterialCapability",
    "NumericTolerance",
    "OperationTarget",
    "PathReference",
    "PersonalisationCapability",
    "PhysicalRequirementDecision",
    "Point2D",
    "PrintComponent",
    "PrintJobSpecification",
    "PrintJobSpecificationV04",
    "PrintJobSpecificationV05",
    "PrintOperationParameters",
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
    "PublicCapabilityQuestion",
    "PublicControlledDefaultFoldGeometry",
    "PublicControlledDefaultUserEvidence",
    "PublicControlledInterpretationState",
    "PublicControlledProductionDefault",
    "PublicInterpretationContinuationAnswer",
    "PublicInterpretationFulfilmentState",
    "PublicInterpretationIntent",
    "PublicInterpretationJob",
    "PublicInterpretationQuestion",
    "PublicInterpretationQuestionOption",
    "PublicInterpretationScope",
    "PublicInterpretationTruthState",
    "PublicJobContextFact",
    "PublicJobStructure",
    "PublicMatchTargetRequest",
    "PublicMatchTargetState",
    "PublicProducerUniverseCandidate",
    "PublicRecipeState",
    "PublicSharedContextFact",
    "PublicSpecMatchReadiness",
    "PublicUnderstoodFinishing",
    "PublicUnderstoodPrint",
    "PublicUnderstoodRequirement",
    "PublicUnderstoodSize",
    "PublicUnderstoodSubstrate",
    "PublicUseConditionReview",
    "QualityRequirement",
    "Quantity",
    "QuantityRange",
    "RecipeResource",
    "Rectangle2D",
    "RepeatPatternCapability",
    "RepeatedDrillPattern",
    "ResolveRecipeRequest",
    "ResolveRecipeResponse",
    "ResolvedRecipeMatchState",
    "ServiceRequirements",
    "SourceInput",
    "SpecMatchResult",
    "SpecificationExternalReference",
    "SpecificationFieldProvenance",
    "SpecificationRecipeReference",
    "SpecificationResource",
    "Substrate",
    "SurfaceOperationParameters",
    "TransformRequest",
    "TransformResponse",
    "TurnaroundCapability",
    "UseRequirement",
    "Value",
    "VariationField",
    "WashabilityCapability",
]

# import apis into sdk package
from gnaww_sdk.api.producer_capabilities_api import ProducerCapabilitiesApi as ProducerCapabilitiesApi
from gnaww_sdk.api.recipes_api import RecipesApi as RecipesApi
from gnaww_sdk.api.spec_match_api import SpecMatchApi as SpecMatchApi
from gnaww_sdk.api.specifications_api import SpecificationsApi as SpecificationsApi
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
from gnaww_sdk.models.app_models_manufacturing_geometry_material_composition_part import AppModelsManufacturingGeometryMaterialCompositionPart as AppModelsManufacturingGeometryMaterialCompositionPart
from gnaww_sdk.models.app_models_producer_material_composition_part import AppModelsProducerMaterialCompositionPart as AppModelsProducerMaterialCompositionPart
from gnaww_sdk.models.apparel_decoration_options import ApparelDecorationOptions as ApparelDecorationOptions
from gnaww_sdk.models.apparel_options import ApparelOptions as ApparelOptions
from gnaww_sdk.models.artwork_requirements import ArtworkRequirements as ArtworkRequirements
from gnaww_sdk.models.assembly_operation_parameters import AssemblyOperationParameters as AssemblyOperationParameters
from gnaww_sdk.models.availability_capability import AvailabilityCapability as AvailabilityCapability
from gnaww_sdk.models.benchmark_quantity_guidance import BenchmarkQuantityGuidance as BenchmarkQuantityGuidance
from gnaww_sdk.models.book_document_options import BookDocumentOptions as BookDocumentOptions
from gnaww_sdk.models.capability_evidence import CapabilityEvidence as CapabilityEvidence
from gnaww_sdk.models.circle2_d import Circle2D as Circle2D
from gnaww_sdk.models.colour_capability import ColourCapability as ColourCapability
from gnaww_sdk.models.commercial_print_options import CommercialPrintOptions as CommercialPrintOptions
from gnaww_sdk.models.continue_interpretation_request_v02 import ContinueInterpretationRequestV02 as ContinueInterpretationRequestV02
from gnaww_sdk.models.continue_print_requirement_interpretation_default_response import ContinuePrintRequirementInterpretationDefaultResponse as ContinuePrintRequirementInterpretationDefaultResponse
from gnaww_sdk.models.continue_print_requirement_interpretation_default_response_error import ContinuePrintRequirementInterpretationDefaultResponseError as ContinuePrintRequirementInterpretationDefaultResponseError
from gnaww_sdk.models.contour import Contour as Contour
from gnaww_sdk.models.create_specification_request import CreateSpecificationRequest as CreateSpecificationRequest
from gnaww_sdk.models.create_specification_response import CreateSpecificationResponse as CreateSpecificationResponse
from gnaww_sdk.models.custom_dimension_capability import CustomDimensionCapability as CustomDimensionCapability
from gnaww_sdk.models.cut_operation_parameters import CutOperationParameters as CutOperationParameters
from gnaww_sdk.models.decoration_area_capability import DecorationAreaCapability as DecorationAreaCapability
from gnaww_sdk.models.decoration_operation_parameters import DecorationOperationParameters as DecorationOperationParameters
from gnaww_sdk.models.delivery_destination import DeliveryDestination as DeliveryDestination
from gnaww_sdk.models.dimension_capability import DimensionCapability as DimensionCapability
from gnaww_sdk.models.drill_hole import DrillHole as DrillHole
from gnaww_sdk.models.drill_operation_parameters import DrillOperationParameters as DrillOperationParameters
from gnaww_sdk.models.edge_relative_point import EdgeRelativePoint as EdgeRelativePoint
from gnaww_sdk.models.fabric_homewares_capability_options import FabricHomewaresCapabilityOptions as FabricHomewaresCapabilityOptions
from gnaww_sdk.models.fabric_homewares_options import FabricHomewaresOptions as FabricHomewaresOptions
from gnaww_sdk.models.finished_size import FinishedSize as FinishedSize
from gnaww_sdk.models.finishing import Finishing as Finishing
from gnaww_sdk.models.fold_line import FoldLine as FoldLine
from gnaww_sdk.models.fold_operation_parameters import FoldOperationParameters as FoldOperationParameters
from gnaww_sdk.models.fold_panel import FoldPanel as FoldPanel
from gnaww_sdk.models.folded_leaflet_options import FoldedLeafletOptions as FoldedLeafletOptions
from gnaww_sdk.models.fulfilment_match_result import FulfilmentMatchResult as FulfilmentMatchResult
from gnaww_sdk.models.fulfilment_requirement import FulfilmentRequirement as FulfilmentRequirement
from gnaww_sdk.models.gjs import Gjs as Gjs
from gnaww_sdk.models.gjs1 import Gjs1 as Gjs1
from gnaww_sdk.models.grammage_requirement import GrammageRequirement as GrammageRequirement
from gnaww_sdk.models.grounded_product_meaning import GroundedProductMeaning as GroundedProductMeaning
from gnaww_sdk.models.health_response import HealthResponse as HealthResponse
from gnaww_sdk.models.inspect_operation_parameters import InspectOperationParameters as InspectOperationParameters
from gnaww_sdk.models.intent_classification_response import IntentClassificationResponse as IntentClassificationResponse
from gnaww_sdk.models.intent_plan_evidence import IntentPlanEvidence as IntentPlanEvidence
from gnaww_sdk.models.intent_provider_metadata import IntentProviderMetadata as IntentProviderMetadata
from gnaww_sdk.models.interpret_print_requirement_default_response import InterpretPrintRequirementDefaultResponse as InterpretPrintRequirementDefaultResponse
from gnaww_sdk.models.interpret_print_requirement_default_response_error import InterpretPrintRequirementDefaultResponseError as InterpretPrintRequirementDefaultResponseError
from gnaww_sdk.models.interpret_print_requirement_request import InterpretPrintRequirementRequest as InterpretPrintRequirementRequest
from gnaww_sdk.models.interpretation_result_v02 import InterpretationResultV02 as InterpretationResultV02
from gnaww_sdk.models.issue import Issue as Issue
from gnaww_sdk.models.issue_set import IssueSet as IssueSet
from gnaww_sdk.models.legacy_operation_parameters import LegacyOperationParameters as LegacyOperationParameters
from gnaww_sdk.models.line2_d import Line2D as Line2D
from gnaww_sdk.models.manufacturing_assembly import ManufacturingAssembly as ManufacturingAssembly
from gnaww_sdk.models.manufacturing_component import ManufacturingComponent as ManufacturingComponent
from gnaww_sdk.models.manufacturing_geometry import ManufacturingGeometry as ManufacturingGeometry
from gnaww_sdk.models.manufacturing_material import ManufacturingMaterial as ManufacturingMaterial
from gnaww_sdk.models.manufacturing_operation import ManufacturingOperation as ManufacturingOperation
from gnaww_sdk.models.manufacturing_operation_parameters import ManufacturingOperationParameters as ManufacturingOperationParameters
from gnaww_sdk.models.manufacturing_quantity import ManufacturingQuantity as ManufacturingQuantity
from gnaww_sdk.models.manufacturing_region import ManufacturingRegion as ManufacturingRegion
from gnaww_sdk.models.manufacturing_region_geometry import ManufacturingRegionGeometry as ManufacturingRegionGeometry
from gnaww_sdk.models.manufacturing_variation import ManufacturingVariation as ManufacturingVariation
from gnaww_sdk.models.match_difference import MatchDifference as MatchDifference
from gnaww_sdk.models.match_print_demand_default_response import MatchPrintDemandDefaultResponse as MatchPrintDemandDefaultResponse
from gnaww_sdk.models.match_print_demand_request import MatchPrintDemandRequest as MatchPrintDemandRequest
from gnaww_sdk.models.match_print_demand_response import MatchPrintDemandResponse as MatchPrintDemandResponse
from gnaww_sdk.models.match_print_demand_universe_request import MatchPrintDemandUniverseRequest as MatchPrintDemandUniverseRequest
from gnaww_sdk.models.match_print_demand_universe_response import MatchPrintDemandUniverseResponse as MatchPrintDemandUniverseResponse
from gnaww_sdk.models.match_recipe_request import MatchRecipeRequest as MatchRecipeRequest
from gnaww_sdk.models.match_recipe_response import MatchRecipeResponse as MatchRecipeResponse
from gnaww_sdk.models.material_capability import MaterialCapability as MaterialCapability
from gnaww_sdk.models.numeric_tolerance import NumericTolerance as NumericTolerance
from gnaww_sdk.models.operation_target import OperationTarget as OperationTarget
from gnaww_sdk.models.path_reference import PathReference as PathReference
from gnaww_sdk.models.personalisation_capability import PersonalisationCapability as PersonalisationCapability
from gnaww_sdk.models.physical_requirement_decision import PhysicalRequirementDecision as PhysicalRequirementDecision
from gnaww_sdk.models.point2_d import Point2D as Point2D
from gnaww_sdk.models.print_component import PrintComponent as PrintComponent
from gnaww_sdk.models.print_job_specification import PrintJobSpecification as PrintJobSpecification
from gnaww_sdk.models.print_job_specification_v04 import PrintJobSpecificationV04 as PrintJobSpecificationV04
from gnaww_sdk.models.print_job_specification_v05 import PrintJobSpecificationV05 as PrintJobSpecificationV05
from gnaww_sdk.models.print_operation_parameters import PrintOperationParameters as PrintOperationParameters
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
from gnaww_sdk.models.public_capability_question import PublicCapabilityQuestion as PublicCapabilityQuestion
from gnaww_sdk.models.public_controlled_default_fold_geometry import PublicControlledDefaultFoldGeometry as PublicControlledDefaultFoldGeometry
from gnaww_sdk.models.public_controlled_default_user_evidence import PublicControlledDefaultUserEvidence as PublicControlledDefaultUserEvidence
from gnaww_sdk.models.public_controlled_interpretation_state import PublicControlledInterpretationState as PublicControlledInterpretationState
from gnaww_sdk.models.public_controlled_production_default import PublicControlledProductionDefault as PublicControlledProductionDefault
from gnaww_sdk.models.public_interpretation_continuation_answer import PublicInterpretationContinuationAnswer as PublicInterpretationContinuationAnswer
from gnaww_sdk.models.public_interpretation_fulfilment_state import PublicInterpretationFulfilmentState as PublicInterpretationFulfilmentState
from gnaww_sdk.models.public_interpretation_intent import PublicInterpretationIntent as PublicInterpretationIntent
from gnaww_sdk.models.public_interpretation_job import PublicInterpretationJob as PublicInterpretationJob
from gnaww_sdk.models.public_interpretation_question import PublicInterpretationQuestion as PublicInterpretationQuestion
from gnaww_sdk.models.public_interpretation_question_option import PublicInterpretationQuestionOption as PublicInterpretationQuestionOption
from gnaww_sdk.models.public_interpretation_scope import PublicInterpretationScope as PublicInterpretationScope
from gnaww_sdk.models.public_interpretation_truth_state import PublicInterpretationTruthState as PublicInterpretationTruthState
from gnaww_sdk.models.public_job_context_fact import PublicJobContextFact as PublicJobContextFact
from gnaww_sdk.models.public_job_structure import PublicJobStructure as PublicJobStructure
from gnaww_sdk.models.public_match_target_request import PublicMatchTargetRequest as PublicMatchTargetRequest
from gnaww_sdk.models.public_match_target_state import PublicMatchTargetState as PublicMatchTargetState
from gnaww_sdk.models.public_producer_universe_candidate import PublicProducerUniverseCandidate as PublicProducerUniverseCandidate
from gnaww_sdk.models.public_recipe_state import PublicRecipeState as PublicRecipeState
from gnaww_sdk.models.public_shared_context_fact import PublicSharedContextFact as PublicSharedContextFact
from gnaww_sdk.models.public_spec_match_readiness import PublicSpecMatchReadiness as PublicSpecMatchReadiness
from gnaww_sdk.models.public_understood_finishing import PublicUnderstoodFinishing as PublicUnderstoodFinishing
from gnaww_sdk.models.public_understood_print import PublicUnderstoodPrint as PublicUnderstoodPrint
from gnaww_sdk.models.public_understood_requirement import PublicUnderstoodRequirement as PublicUnderstoodRequirement
from gnaww_sdk.models.public_understood_size import PublicUnderstoodSize as PublicUnderstoodSize
from gnaww_sdk.models.public_understood_substrate import PublicUnderstoodSubstrate as PublicUnderstoodSubstrate
from gnaww_sdk.models.public_use_condition_review import PublicUseConditionReview as PublicUseConditionReview
from gnaww_sdk.models.quality_requirement import QualityRequirement as QualityRequirement
from gnaww_sdk.models.quantity import Quantity as Quantity
from gnaww_sdk.models.quantity_range import QuantityRange as QuantityRange
from gnaww_sdk.models.recipe_resource import RecipeResource as RecipeResource
from gnaww_sdk.models.rectangle2_d import Rectangle2D as Rectangle2D
from gnaww_sdk.models.repeat_pattern_capability import RepeatPatternCapability as RepeatPatternCapability
from gnaww_sdk.models.repeated_drill_pattern import RepeatedDrillPattern as RepeatedDrillPattern
from gnaww_sdk.models.resolve_recipe_request import ResolveRecipeRequest as ResolveRecipeRequest
from gnaww_sdk.models.resolve_recipe_response import ResolveRecipeResponse as ResolveRecipeResponse
from gnaww_sdk.models.resolved_recipe_match_state import ResolvedRecipeMatchState as ResolvedRecipeMatchState
from gnaww_sdk.models.service_requirements import ServiceRequirements as ServiceRequirements
from gnaww_sdk.models.source_input import SourceInput as SourceInput
from gnaww_sdk.models.spec_match_result import SpecMatchResult as SpecMatchResult
from gnaww_sdk.models.specification_external_reference import SpecificationExternalReference as SpecificationExternalReference
from gnaww_sdk.models.specification_field_provenance import SpecificationFieldProvenance as SpecificationFieldProvenance
from gnaww_sdk.models.specification_recipe_reference import SpecificationRecipeReference as SpecificationRecipeReference
from gnaww_sdk.models.specification_resource import SpecificationResource as SpecificationResource
from gnaww_sdk.models.substrate import Substrate as Substrate
from gnaww_sdk.models.surface_operation_parameters import SurfaceOperationParameters as SurfaceOperationParameters
from gnaww_sdk.models.transform_request import TransformRequest as TransformRequest
from gnaww_sdk.models.transform_response import TransformResponse as TransformResponse
from gnaww_sdk.models.turnaround_capability import TurnaroundCapability as TurnaroundCapability
from gnaww_sdk.models.use_requirement import UseRequirement as UseRequirement
from gnaww_sdk.models.value import Value as Value
from gnaww_sdk.models.variation_field import VariationField as VariationField
from gnaww_sdk.models.washability_capability import WashabilityCapability as WashabilityCapability
from gnaww_sdk.convenience import (
    GnawwApiError,
    GnawwClarificationAnswer,
    GnawwClient,
    GnawwPublicError,
    GnawwResponse,
)
