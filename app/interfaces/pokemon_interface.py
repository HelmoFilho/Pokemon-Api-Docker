## -- Importing External Modules -- ##
from pydantic import BaseModel, Field, root_validator, validator
from fastapi import HTTPException
from enum import Enum, auto

## -- Importing Internal Modules -- ##

## Request
class Pokemon(BaseModel):

    id: int = Field(
        None,
        description = "Pokemon`s national dex number",
        gt = 0,
    )
    name: str = Field(
        None,
        description = "Pokemon`s name",
        min_lenght = 0,
    )

    @validator("name", pre = True)
    def lower_name(cls, value):
        
        if isinstance(value, str):
            return value.lower()

        return value

    @root_validator()
    def check_existence(cls, fields):

        id = fields.get("id")
        name = fields.get("name")

        if not (id or name):
            raise HTTPException(
                    status_code = 400,
                    detail = "name or id should be provided."
                )

        if (id and name):
            raise HTTPException(
                    status_code = 400,
                    detail = "name or id should be provided alone."
                )

        return fields

    class Config:

        schema_extra = {
            "example": {
                "name": "Gholdengo",
            }
        }


## Response   
class Status(Enum):

    def _generate_next_value_(name, start, count, last_values):
        return name.lower()

    SUCCESS = auto()
    ERROR = auto()

class BaseResponse(BaseModel):

    status: Status = Field(
        None,
        description = "If the request was a success or not."
    )
    description: str = Field(
        None,
        description = "A message describing the results of the request"
    )


class ErrorResponse(BaseResponse):

    class Config:

        schema_extra = {
            "example": {
                "stats": "error",
                "description": "Pokemon not found.",
            }
        }


class DataResponse(BaseModel):

    name: str = Field(
        ...,
        description = "Pokemon`s name capitalized." 
    )
    info: dict = Field(
        ...,
        description = "All of the pokemon`s info."
    )

class SuccessResponse(BaseResponse):

    data: DataResponse = Field(
        ...,
        description = "Information about the required pokemon."
    )

    class Config:

        schema_extra = {
            "example": {
                "status": "success",
                "message": "Pokemon info was found.",
                "data": {
                    "name": "Gholdengo",
                    "info": {
                        "abilities": [
                            {
                                "ability": {
                                    "name": "good-as-gold",
                                    "url": "https://pokeapi.co/api/v2/ability/283/"
                                },
                                "is_hidden": False,
                                "slot": 1
                            },
                            {
                                "ability": {
                                    "name": "good-as-gold",
                                    "url": "https://pokeapi.co/api/v2/ability/283/"
                                },
                                "is_hidden": True,
                                "slot": 3
                            }
                        ],
                        "base_experience": None,
                        "forms": [
                            {
                                "name": "gholdengo",
                                "url": "https://pokeapi.co/api/v2/pokemon-form/1000/"
                            }
                        ],
                        "game_indices": [],
                        "height": 12,
                        "held_items": [],
                        "id": 1000,
                        "is_default": True,
                        "location_area_encounters": "https://pokeapi.co/api/v2/pokemon/1000/encounters",
                        "moves": [
                            {
                                "move": {
                                    "name": "thunder-punch",
                                    "url": "https://pokeapi.co/api/v2/move/9/"
                                },
                                "version_group_details": [
                                    {
                                        "level_learned_at": 0,
                                        "move_learn_method": {
                                            "name": "machine",
                                            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
                                        },
                                        "version_group": {
                                            "name": "scarlet-violet",
                                            "url": "https://pokeapi.co/api/v2/version-group/25/"
                                        }
                                    }
                                ]
                            },
                            {
                                "move": {
                                    "name": "tackle",
                                    "url": "https://pokeapi.co/api/v2/move/33/"
                                },
                                "version_group_details": [
                                    {
                                        "level_learned_at": 1,
                                        "move_learn_method": {
                                            "name": "level-up",
                                            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
                                        },
                                        "version_group": {
                                            "name": "scarlet-violet",
                                            "url": "https://pokeapi.co/api/v2/version-group/25/"
                                        }
                                    }
                                ]
                            },
                            {
                                "move": {
                                    "name": "take-down",
                                    "url": "https://pokeapi.co/api/v2/move/36/"
                                },
                                "version_group_details": [
                                    {
                                        "level_learned_at": 0,
                                        "move_learn_method": {
                                            "name": "machine",
                                            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
                                        },
                                        "version_group": {
                                            "name": "scarlet-violet",
                                            "url": "https://pokeapi.co/api/v2/version-group/25/"
                                        }
                                    }
                                ]
                            },
                            {
                                "move": {
                                    "name": "hyper-beam",
                                    "url": "https://pokeapi.co/api/v2/move/63/"
                                },
                                "version_group_details": [
                                    {
                                        "level_learned_at": 0,
                                        "move_learn_method": {
                                            "name": "machine",
                                            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
                                        },
                                        "version_group": {
                                            "name": "scarlet-violet",
                                            "url": "https://pokeapi.co/api/v2/version-group/25/"
                                        }
                                    }
                                ]
                            },
                            {
                                "move": {
                                    "name": "low-kick",
                                    "url": "https://pokeapi.co/api/v2/move/67/"
                                },
                                "version_group_details": [
                                    {
                                        "level_learned_at": 0,
                                        "move_learn_method": {
                                            "name": "machine",
                                            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
                                        },
                                        "version_group": {
                                            "name": "scarlet-violet",
                                            "url": "https://pokeapi.co/api/v2/version-group/25/"
                                        }
                                    }
                                ]
                            },
                            {
                                "move": {
                                    "name": "thunderbolt",
                                    "url": "https://pokeapi.co/api/v2/move/85/"
                                },
                                "version_group_details": [
                                    {
                                        "level_learned_at": 0,
                                        "move_learn_method": {
                                            "name": "machine",
                                            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
                                        },
                                        "version_group": {
                                            "name": "scarlet-violet",
                                            "url": "https://pokeapi.co/api/v2/version-group/25/"
                                        }
                                    }
                                ]
                            },
                            {
                                "move": {
                                    "name": "thunder-wave",
                                    "url": "https://pokeapi.co/api/v2/move/86/"
                                },
                                "version_group_details": [
                                    {
                                        "level_learned_at": 0,
                                        "move_learn_method": {
                                            "name": "machine",
                                            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
                                        },
                                        "version_group": {
                                            "name": "scarlet-violet",
                                            "url": "https://pokeapi.co/api/v2/version-group/25/"
                                        }
                                    }
                                ]
                            },
                            {
                                "move": {
                                    "name": "thunder",
                                    "url": "https://pokeapi.co/api/v2/move/87/"
                                },
                                "version_group_details": [
                                    {
                                        "level_learned_at": 0,
                                        "move_learn_method": {
                                            "name": "machine",
                                            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
                                        },
                                        "version_group": {
                                            "name": "scarlet-violet",
                                            "url": "https://pokeapi.co/api/v2/version-group/25/"
                                        }
                                    }
                                ]
                            },
                            {
                                "move": {
                                    "name": "psychic",
                                    "url": "https://pokeapi.co/api/v2/move/94/"
                                },
                                "version_group_details": [
                                    {
                                        "level_learned_at": 0,
                                        "move_learn_method": {
                                            "name": "machine",
                                            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
                                        },
                                        "version_group": {
                                            "name": "scarlet-violet",
                                            "url": "https://pokeapi.co/api/v2/version-group/25/"
                                        }
                                    }
                                ]
                            },
                            {
                                "move": {
                                    "name": "night-shade",
                                    "url": "https://pokeapi.co/api/v2/move/101/"
                                },
                                "version_group_details": [
                                    {
                                        "level_learned_at": 7,
                                        "move_learn_method": {
                                            "name": "level-up",
                                            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
                                        },
                                        "version_group": {
                                            "name": "scarlet-violet",
                                            "url": "https://pokeapi.co/api/v2/version-group/25/"
                                        }
                                    },
                                    {
                                        "level_learned_at": 0,
                                        "move_learn_method": {
                                            "name": "machine",
                                            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
                                        },
                                        "version_group": {
                                            "name": "scarlet-violet",
                                            "url": "https://pokeapi.co/api/v2/version-group/25/"
                                        }
                                    }
                                ]
                            },
                            {
                                "move": {
                                    "name": "recover",
                                    "url": "https://pokeapi.co/api/v2/move/105/"
                                },
                                "version_group_details": [
                                    {
                                        "level_learned_at": 42,
                                        "move_learn_method": {
                                            "name": "level-up",
                                            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
                                        },
                                        "version_group": {
                                            "name": "scarlet-violet",
                                            "url": "https://pokeapi.co/api/v2/version-group/25/"
                                        }
                                    }
                                ]
                            },
                            {
                                "move": {
                                    "name": "confuse-ray",
                                    "url": "https://pokeapi.co/api/v2/move/109/"
                                },
                                "version_group_details": [
                                    {
                                        "level_learned_at": 14,
                                        "move_learn_method": {
                                            "name": "level-up",
                                            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
                                        },
                                        "version_group": {
                                            "name": "scarlet-violet",
                                            "url": "https://pokeapi.co/api/v2/version-group/25/"
                                        }
                                    },
                                    {
                                        "level_learned_at": 0,
                                        "move_learn_method": {
                                            "name": "machine",
                                            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
                                        },
                                        "version_group": {
                                            "name": "scarlet-violet",
                                            "url": "https://pokeapi.co/api/v2/version-group/25/"
                                        }
                                    }
                                ]
                            },
                            {
                                "move": {
                                    "name": "light-screen",
                                    "url": "https://pokeapi.co/api/v2/move/113/"
                                },
                                "version_group_details": [
                                    {
                                        "level_learned_at": 0,
                                        "move_learn_method": {
                                            "name": "machine",
                                            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
                                        },
                                        "version_group": {
                                            "name": "scarlet-violet",
                                            "url": "https://pokeapi.co/api/v2/version-group/25/"
                                        }
                                    }
                                ]
                            },
                            {
                                "move": {
                                    "name": "reflect",
                                    "url": "https://pokeapi.co/api/v2/move/115/"
                                },
                                "version_group_details": [
                                    {
                                        "level_learned_at": 0,
                                        "move_learn_method": {
                                            "name": "machine",
                                            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
                                        },
                                        "version_group": {
                                            "name": "scarlet-violet",
                                            "url": "https://pokeapi.co/api/v2/version-group/25/"
                                        }
                                    }
                                ]
                            },
                            {
                                "move": {
                                    "name": "rest",
                                    "url": "https://pokeapi.co/api/v2/move/156/"
                                },
                                "version_group_details": [
                                    {
                                        "level_learned_at": 0,
                                        "move_learn_method": {
                                            "name": "machine",
                                            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
                                        },
                                        "version_group": {
                                            "name": "scarlet-violet",
                                            "url": "https://pokeapi.co/api/v2/version-group/25/"
                                        }
                                    }
                                ]
                            },
                            {
                                "move": {
                                    "name": "substitute",
                                    "url": "https://pokeapi.co/api/v2/move/164/"
                                },
                                "version_group_details": [
                                    {
                                        "level_learned_at": 21,
                                        "move_learn_method": {
                                            "name": "level-up",
                                            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
                                        },
                                        "version_group": {
                                            "name": "scarlet-violet",
                                            "url": "https://pokeapi.co/api/v2/version-group/25/"
                                        }
                                    },
                                    {
                                        "level_learned_at": 0,
                                        "move_learn_method": {
                                            "name": "machine",
                                            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
                                        },
                                        "version_group": {
                                            "name": "scarlet-violet",
                                            "url": "https://pokeapi.co/api/v2/version-group/25/"
                                        }
                                    }
                                ]
                            },
                            {
                                "move": {
                                    "name": "thief",
                                    "url": "https://pokeapi.co/api/v2/move/168/"
                                },
                                "version_group_details": [
                                    {
                                        "level_learned_at": 0,
                                        "move_learn_method": {
                                            "name": "machine",
                                            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
                                        },
                                        "version_group": {
                                            "name": "scarlet-violet",
                                            "url": "https://pokeapi.co/api/v2/version-group/25/"
                                        }
                                    }
                                ]
                            },
                            {
                                "move": {
                                    "name": "protect",
                                    "url": "https://pokeapi.co/api/v2/move/182/"
                                },
                                "version_group_details": [
                                    {
                                        "level_learned_at": 0,
                                        "move_learn_method": {
                                            "name": "machine",
                                            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
                                        },
                                        "version_group": {
                                            "name": "scarlet-violet",
                                            "url": "https://pokeapi.co/api/v2/version-group/25/"
                                        }
                                    }
                                ]
                            },
                            {
                                "move": {
                                    "name": "sandstorm",
                                    "url": "https://pokeapi.co/api/v2/move/201/"
                                },
                                "version_group_details": [
                                    {
                                        "level_learned_at": 0,
                                        "move_learn_method": {
                                            "name": "machine",
                                            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
                                        },
                                        "version_group": {
                                            "name": "scarlet-violet",
                                            "url": "https://pokeapi.co/api/v2/version-group/25/"
                                        }
                                    }
                                ]
                            },
                            {
                                "move": {
                                    "name": "endure",
                                    "url": "https://pokeapi.co/api/v2/move/203/"
                                },
                                "version_group_details": [
                                    {
                                        "level_learned_at": 0,
                                        "move_learn_method": {
                                            "name": "machine",
                                            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
                                        },
                                        "version_group": {
                                            "name": "scarlet-violet",
                                            "url": "https://pokeapi.co/api/v2/version-group/25/"
                                        }
                                    }
                                ]
                            },
                            {
                                "move": {
                                    "name": "sleep-talk",
                                    "url": "https://pokeapi.co/api/v2/move/214/"
                                },
                                "version_group_details": [
                                    {
                                        "level_learned_at": 0,
                                        "move_learn_method": {
                                            "name": "machine",
                                            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
                                        },
                                        "version_group": {
                                            "name": "scarlet-violet",
                                            "url": "https://pokeapi.co/api/v2/version-group/25/"
                                        }
                                    }
                                ]
                            },
                            {
                                "move": {
                                    "name": "shadow-ball",
                                    "url": "https://pokeapi.co/api/v2/move/247/"
                                },
                                "version_group_details": [
                                    {
                                        "level_learned_at": 35,
                                        "move_learn_method": {
                                            "name": "level-up",
                                            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
                                        },
                                        "version_group": {
                                            "name": "scarlet-violet",
                                            "url": "https://pokeapi.co/api/v2/version-group/25/"
                                        }
                                    },
                                    {
                                        "level_learned_at": 0,
                                        "move_learn_method": {
                                            "name": "machine",
                                            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
                                        },
                                        "version_group": {
                                            "name": "scarlet-violet",
                                            "url": "https://pokeapi.co/api/v2/version-group/25/"
                                        }
                                    }
                                ]
                            },
                            {
                                "move": {
                                    "name": "memento",
                                    "url": "https://pokeapi.co/api/v2/move/262/"
                                },
                                "version_group_details": [
                                    {
                                        "level_learned_at": 70,
                                        "move_learn_method": {
                                            "name": "level-up",
                                            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
                                        },
                                        "version_group": {
                                            "name": "scarlet-violet",
                                            "url": "https://pokeapi.co/api/v2/version-group/25/"
                                        }
                                    }
                                ]
                            },
                            {
                                "move": {
                                    "name": "trick",
                                    "url": "https://pokeapi.co/api/v2/move/271/"
                                },
                                "version_group_details": [
                                    {
                                        "level_learned_at": 0,
                                        "move_learn_method": {
                                            "name": "machine",
                                            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
                                        },
                                        "version_group": {
                                            "name": "scarlet-violet",
                                            "url": "https://pokeapi.co/api/v2/version-group/25/"
                                        }
                                    }
                                ]
                            },
                            {
                                "move": {
                                    "name": "astonish",
                                    "url": "https://pokeapi.co/api/v2/move/310/"
                                },
                                "version_group_details": [
                                    {
                                        "level_learned_at": 1,
                                        "move_learn_method": {
                                            "name": "level-up",
                                            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
                                        },
                                        "version_group": {
                                            "name": "scarlet-violet",
                                            "url": "https://pokeapi.co/api/v2/version-group/25/"
                                        }
                                    }
                                ]
                            },
                            {
                                "move": {
                                    "name": "metal-sound",
                                    "url": "https://pokeapi.co/api/v2/move/319/"
                                },
                                "version_group_details": [
                                    {
                                        "level_learned_at": 28,
                                        "move_learn_method": {
                                            "name": "level-up",
                                            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
                                        },
                                        "version_group": {
                                            "name": "scarlet-violet",
                                            "url": "https://pokeapi.co/api/v2/version-group/25/"
                                        }
                                    }
                                ]
                            },
                            {
                                "move": {
                                    "name": "fling",
                                    "url": "https://pokeapi.co/api/v2/move/374/"
                                },
                                "version_group_details": [
                                    {
                                        "level_learned_at": 0,
                                        "move_learn_method": {
                                            "name": "machine",
                                            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
                                        },
                                        "version_group": {
                                            "name": "scarlet-violet",
                                            "url": "https://pokeapi.co/api/v2/version-group/25/"
                                        }
                                    }
                                ]
                            },
                            {
                                "move": {
                                    "name": "power-gem",
                                    "url": "https://pokeapi.co/api/v2/move/408/"
                                },
                                "version_group_details": [
                                    {
                                        "level_learned_at": 49,
                                        "move_learn_method": {
                                            "name": "level-up",
                                            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
                                        },
                                        "version_group": {
                                            "name": "scarlet-violet",
                                            "url": "https://pokeapi.co/api/v2/version-group/25/"
                                        }
                                    },
                                    {
                                        "level_learned_at": 0,
                                        "move_learn_method": {
                                            "name": "machine",
                                            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
                                        },
                                        "version_group": {
                                            "name": "scarlet-violet",
                                            "url": "https://pokeapi.co/api/v2/version-group/25/"
                                        }
                                    }
                                ]
                            },
                            {
                                "move": {
                                    "name": "focus-blast",
                                    "url": "https://pokeapi.co/api/v2/move/411/"
                                },
                                "version_group_details": [
                                    {
                                        "level_learned_at": 0,
                                        "move_learn_method": {
                                            "name": "machine",
                                            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
                                        },
                                        "version_group": {
                                            "name": "scarlet-violet",
                                            "url": "https://pokeapi.co/api/v2/version-group/25/"
                                        }
                                    }
                                ]
                            },
                            {
                                "move": {
                                    "name": "giga-impact",
                                    "url": "https://pokeapi.co/api/v2/move/416/"
                                },
                                "version_group_details": [
                                    {
                                        "level_learned_at": 0,
                                        "move_learn_method": {
                                            "name": "machine",
                                            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
                                        },
                                        "version_group": {
                                            "name": "scarlet-violet",
                                            "url": "https://pokeapi.co/api/v2/version-group/25/"
                                        }
                                    }
                                ]
                            },
                            {
                                "move": {
                                    "name": "nasty-plot",
                                    "url": "https://pokeapi.co/api/v2/move/417/"
                                },
                                "version_group_details": [
                                    {
                                        "level_learned_at": 63,
                                        "move_learn_method": {
                                            "name": "level-up",
                                            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
                                        },
                                        "version_group": {
                                            "name": "scarlet-violet",
                                            "url": "https://pokeapi.co/api/v2/version-group/25/"
                                        }
                                    },
                                    {
                                        "level_learned_at": 0,
                                        "move_learn_method": {
                                            "name": "machine",
                                            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
                                        },
                                        "version_group": {
                                            "name": "scarlet-violet",
                                            "url": "https://pokeapi.co/api/v2/version-group/25/"
                                        }
                                    }
                                ]
                            },
                            {
                                "move": {
                                    "name": "flash-cannon",
                                    "url": "https://pokeapi.co/api/v2/move/430/"
                                },
                                "version_group_details": [
                                    {
                                        "level_learned_at": 0,
                                        "move_learn_method": {
                                            "name": "machine",
                                            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
                                        },
                                        "version_group": {
                                            "name": "scarlet-violet",
                                            "url": "https://pokeapi.co/api/v2/version-group/25/"
                                        }
                                    }
                                ]
                            },
                            {
                                "move": {
                                    "name": "iron-head",
                                    "url": "https://pokeapi.co/api/v2/move/442/"
                                },
                                "version_group_details": [
                                    {
                                        "level_learned_at": 0,
                                        "move_learn_method": {
                                            "name": "machine",
                                            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
                                        },
                                        "version_group": {
                                            "name": "scarlet-violet",
                                            "url": "https://pokeapi.co/api/v2/version-group/25/"
                                        }
                                    }
                                ]
                            },
                            {
                                "move": {
                                    "name": "charge-beam",
                                    "url": "https://pokeapi.co/api/v2/move/451/"
                                },
                                "version_group_details": [
                                    {
                                        "level_learned_at": 0,
                                        "move_learn_method": {
                                            "name": "machine",
                                            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
                                        },
                                        "version_group": {
                                            "name": "scarlet-violet",
                                            "url": "https://pokeapi.co/api/v2/version-group/25/"
                                        }
                                    }
                                ]
                            },
                            {
                                "move": {
                                    "name": "psyshock",
                                    "url": "https://pokeapi.co/api/v2/move/473/"
                                },
                                "version_group_details": [
                                    {
                                        "level_learned_at": 0,
                                        "move_learn_method": {
                                            "name": "machine",
                                            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
                                        },
                                        "version_group": {
                                            "name": "scarlet-violet",
                                            "url": "https://pokeapi.co/api/v2/version-group/25/"
                                        }
                                    }
                                ]
                            },
                            {
                                "move": {
                                    "name": "heavy-slam",
                                    "url": "https://pokeapi.co/api/v2/move/484/"
                                },
                                "version_group_details": [
                                    {
                                        "level_learned_at": 0,
                                        "move_learn_method": {
                                            "name": "machine",
                                            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
                                        },
                                        "version_group": {
                                            "name": "scarlet-violet",
                                            "url": "https://pokeapi.co/api/v2/version-group/25/"
                                        }
                                    }
                                ]
                            },
                            {
                                "move": {
                                    "name": "electro-ball",
                                    "url": "https://pokeapi.co/api/v2/move/486/"
                                },
                                "version_group_details": [
                                    {
                                        "level_learned_at": 0,
                                        "move_learn_method": {
                                            "name": "machine",
                                            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
                                        },
                                        "version_group": {
                                            "name": "scarlet-violet",
                                            "url": "https://pokeapi.co/api/v2/version-group/25/"
                                        }
                                    }
                                ]
                            },
                            {
                                "move": {
                                    "name": "low-sweep",
                                    "url": "https://pokeapi.co/api/v2/move/490/"
                                },
                                "version_group_details": [
                                    {
                                        "level_learned_at": 0,
                                        "move_learn_method": {
                                            "name": "machine",
                                            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
                                        },
                                        "version_group": {
                                            "name": "scarlet-violet",
                                            "url": "https://pokeapi.co/api/v2/version-group/25/"
                                        }
                                    }
                                ]
                            },
                            {
                                "move": {
                                    "name": "hex",
                                    "url": "https://pokeapi.co/api/v2/move/506/"
                                },
                                "version_group_details": [
                                    {
                                        "level_learned_at": 0,
                                        "move_learn_method": {
                                            "name": "machine",
                                            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
                                        },
                                        "version_group": {
                                            "name": "scarlet-violet",
                                            "url": "https://pokeapi.co/api/v2/version-group/25/"
                                        }
                                    }
                                ]
                            },
                            {
                                "move": {
                                    "name": "dazzling-gleam",
                                    "url": "https://pokeapi.co/api/v2/move/605/"
                                },
                                "version_group_details": [
                                    {
                                        "level_learned_at": 0,
                                        "move_learn_method": {
                                            "name": "machine",
                                            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
                                        },
                                        "version_group": {
                                            "name": "scarlet-violet",
                                            "url": "https://pokeapi.co/api/v2/version-group/25/"
                                        }
                                    }
                                ]
                            },
                            {
                                "move": {
                                    "name": "steel-beam",
                                    "url": "https://pokeapi.co/api/v2/move/796/"
                                },
                                "version_group_details": [
                                    {
                                        "level_learned_at": 0,
                                        "move_learn_method": {
                                            "name": "machine",
                                            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
                                        },
                                        "version_group": {
                                            "name": "scarlet-violet",
                                            "url": "https://pokeapi.co/api/v2/version-group/25/"
                                        }
                                    }
                                ]
                            },
                            {
                                "move": {
                                    "name": "tera-blast",
                                    "url": "https://pokeapi.co/api/v2/move/851/"
                                },
                                "version_group_details": [
                                    {
                                        "level_learned_at": 0,
                                        "move_learn_method": {
                                            "name": "machine",
                                            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
                                        },
                                        "version_group": {
                                            "name": "scarlet-violet",
                                            "url": "https://pokeapi.co/api/v2/version-group/25/"
                                        }
                                    }
                                ]
                            },
                            {
                                "move": {
                                    "name": "make-it-rain",
                                    "url": "https://pokeapi.co/api/v2/move/874/"
                                },
                                "version_group_details": [
                                    {
                                        "level_learned_at": 56,
                                        "move_learn_method": {
                                            "name": "level-up",
                                            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
                                        },
                                        "version_group": {
                                            "name": "scarlet-violet",
                                            "url": "https://pokeapi.co/api/v2/version-group/25/"
                                        }
                                    }
                                ]
                            }
                        ],
                        "name": "gholdengo",
                        "order": 977,
                        "past_types": [],
                        "species": {
                            "name": "gholdengo",
                            "url": "https://pokeapi.co/api/v2/pokemon-species/1000/"
                        },
                        "sprites": {
                            "back_default": None,
                            "back_female": None,
                            "back_shiny": None,
                            "back_shiny_female": None,
                            "front_default": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/1000.png",
                            "front_female": None,
                            "front_shiny": None,
                            "front_shiny_female": None,
                            "other": {
                                "dream_world": {
                                    "front_default": None,
                                    "front_female": None
                                },
                                "home": {
                                    "front_default": None,
                                    "front_female": None,
                                    "front_shiny": None,
                                    "front_shiny_female": None
                                },
                                "official-artwork": {
                                    "front_default": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/1000.png",
                                    "front_shiny": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/shiny/1000.png"
                                }
                            },
                            "versions": {
                                "generation-i": {
                                    "red-blue": {
                                        "back_default": None,
                                        "back_gray": None,
                                        "back_transparent": None,
                                        "front_default": None,
                                        "front_gray": None,
                                        "front_transparent": None
                                    },
                                    "yellow": {
                                        "back_default": None,
                                        "back_gray": None,
                                        "back_transparent": None,
                                        "front_default": None,
                                        "front_gray": None,
                                        "front_transparent": None
                                    }
                                },
                                "generation-ii": {
                                    "crystal": {
                                        "back_default": None,
                                        "back_shiny": None,
                                        "back_shiny_transparent": None,
                                        "back_transparent": None,
                                        "front_default": None,
                                        "front_shiny": None,
                                        "front_shiny_transparent": None,
                                        "front_transparent": None
                                    },
                                    "gold": {
                                        "back_default": None,
                                        "back_shiny": None,
                                        "front_default": None,
                                        "front_shiny": None,
                                        "front_transparent": None
                                    },
                                    "silver": {
                                        "back_default": None,
                                        "back_shiny": None,
                                        "front_default": None,
                                        "front_shiny": None,
                                        "front_transparent": None
                                    }
                                },
                                "generation-iii": {
                                    "emerald": {
                                        "front_default": None,
                                        "front_shiny": None
                                    },
                                    "firered-leafgreen": {
                                        "back_default": None,
                                        "back_shiny": None,
                                        "front_default": None,
                                        "front_shiny": None
                                    },
                                    "ruby-sapphire": {
                                        "back_default": None,
                                        "back_shiny": None,
                                        "front_default": None,
                                        "front_shiny": None
                                    }
                                },
                                "generation-iv": {
                                    "diamond-pearl": {
                                        "back_default": None,
                                        "back_female": None,
                                        "back_shiny": None,
                                        "back_shiny_female": None,
                                        "front_default": None,
                                        "front_female": None,
                                        "front_shiny": None,
                                        "front_shiny_female": None
                                    },
                                    "heartgold-soulsilver": {
                                        "back_default": None,
                                        "back_female": None,
                                        "back_shiny": None,
                                        "back_shiny_female": None,
                                        "front_default": None,
                                        "front_female": None,
                                        "front_shiny": None,
                                        "front_shiny_female": None
                                    },
                                    "platinum": {
                                        "back_default": None,
                                        "back_female": None,
                                        "back_shiny": None,
                                        "back_shiny_female": None,
                                        "front_default": None,
                                        "front_female": None,
                                        "front_shiny": None,
                                        "front_shiny_female": None
                                    }
                                },
                                "generation-v": {
                                    "black-white": {
                                        "animated": {
                                            "back_default": None,
                                            "back_female": None,
                                            "back_shiny": None,
                                            "back_shiny_female": None,
                                            "front_default": None,
                                            "front_female": None,
                                            "front_shiny": None,
                                            "front_shiny_female": None
                                        },
                                        "back_default": None,
                                        "back_female": None,
                                        "back_shiny": None,
                                        "back_shiny_female": None,
                                        "front_default": None,
                                        "front_female": None,
                                        "front_shiny": None,
                                        "front_shiny_female": None
                                    }
                                },
                                "generation-vi": {
                                    "omegaruby-alphasapphire": {
                                        "front_default": None,
                                        "front_female": None,
                                        "front_shiny": None,
                                        "front_shiny_female": None
                                    },
                                    "x-y": {
                                        "front_default": None,
                                        "front_female": None,
                                        "front_shiny": None,
                                        "front_shiny_female": None
                                    }
                                },
                                "generation-vii": {
                                    "icons": {
                                        "front_default": None,
                                        "front_female": None
                                    },
                                    "ultra-sun-ultra-moon": {
                                        "front_default": None,
                                        "front_female": None,
                                        "front_shiny": None,
                                        "front_shiny_female": None
                                    }
                                },
                                "generation-viii": {
                                    "icons": {
                                        "front_default": None,
                                        "front_female": None
                                    }
                                }
                            }
                        },
                        "stats": [
                            {
                                "base_stat": 87,
                                "effort": 0,
                                "stat": {
                                    "name": "hp",
                                    "url": "https://pokeapi.co/api/v2/stat/1/"
                                }
                            },
                            {
                                "base_stat": 60,
                                "effort": 0,
                                "stat": {
                                    "name": "attack",
                                    "url": "https://pokeapi.co/api/v2/stat/2/"
                                }
                            },
                            {
                                "base_stat": 95,
                                "effort": 0,
                                "stat": {
                                    "name": "defense",
                                    "url": "https://pokeapi.co/api/v2/stat/3/"
                                }
                            },
                            {
                                "base_stat": 133,
                                "effort": 2,
                                "stat": {
                                    "name": "special-attack",
                                    "url": "https://pokeapi.co/api/v2/stat/4/"
                                }
                            },
                            {
                                "base_stat": 91,
                                "effort": 0,
                                "stat": {
                                    "name": "special-defense",
                                    "url": "https://pokeapi.co/api/v2/stat/5/"
                                }
                            },
                            {
                                "base_stat": 84,
                                "effort": 0,
                                "stat": {
                                    "name": "speed",
                                    "url": "https://pokeapi.co/api/v2/stat/6/"
                                }
                            }
                        ],
                        "types": [
                            {
                                "slot": 1,
                                "type": {
                                    "name": "steel",
                                    "url": "https://pokeapi.co/api/v2/type/9/"
                                }
                            },
                            {
                                "slot": 2,
                                "type": {
                                    "name": "ghost",
                                    "url": "https://pokeapi.co/api/v2/type/8/"
                                }
                            }
                        ],
                        "weight": 300
                    }
                }
            }
        }