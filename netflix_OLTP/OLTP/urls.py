from rest_framework.routers import SimpleRouter
from .views import UserViewSet, ShowViewSet, RatingsViewSet, PlanViewSet, DirectorViewSet, RuntimeViewSet, GenreViewSet, PaymentViewSet, BudgetViewSet, ReviewsViewSet

router = SimpleRouter()
router.register("User", UserViewSet)
router.register("Show",ShowViewSet)
router.register("Ratings", RatingsViewSet)
router.register("Plan", PlanViewSet)
router.register("Director", DirectorViewSet)
router.register("Runtime", RuntimeViewSet)
router.register("Genre", GenreViewSet)
router.register("Payment", PaymentViewSet)
router.register("Budget", BudgetViewSet)
router.register("Reviews", ReviewsViewSet)
urlpatterns = router.urls
