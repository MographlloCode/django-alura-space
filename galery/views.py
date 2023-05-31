from django.shortcuts import render, get_object_or_404
from galery.models import Picture


def index(request):

    data = {
        1: {"name": "Alpha's Nebula", "description": "GalaxyExplore.com / Alpha Vega / StarFinder"},
        2: {"name": "Luna's Aurora", "description": "SpaceVision.net / Luna Anderson / MoonScope"},
        3: {"name": "Nova's Cosmos", "description": "StellarAdventures.com / Nova Patel / AstroQuest"},
        4: {"name": "Orion's Galaxy", "description": "AstroExplorers.org / Orion Thompson / Cosmoscope"},
        5: {"name": "Celeste's Stardust", "description": "SkyWonders.com / Celeste Ramirez / StarGaze"},
        6: {"name": "Vega's Cosmos", "description": "StarSearch.net / Vega Li / AstroLens"},
        7: {"name": "Aurora's Nebula", "description": "GalacticVisions.com / Aurora Kim / NebulaScope"},
        8: {"name": "Sirius's Stardust", "description": "CelestialAdventures.org / Sirius Chen / SkyGlimpse"},
        9: {"name": "Stella's Cosmos", "description": "AstroJourneys.com / Stella Johnson / StarGazer"},
        10: {"name": "Solaris's Aurora", "description": "CosmicExplorations.net / Solaris Garcia / AuroraLens"},
    }

    pictures = Picture.objects.all()

    return render(request, 'galery/index.html', {"cards": pictures})

def image(request, picture_id):

    picture = get_object_or_404(Picture, pk=picture_id)

    return render(request, 'galery/image.html', {'picture': picture})