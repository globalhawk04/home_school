import random
import os
import webbrowser

# ---------------------------------------------------------
# 1. THE WORD BANK
# You can add or remove words from this list as needed.
# ---------------------------------------------------------
word_list = [
    # --- Original List ---
    "abundant", "adventure", "ancient", "bizarre", "brilliant",
    "courage", "curious", "delicate", "discovery", "enormous",
    "extraordinary", "fabulous", "ferocious", "generous", "glorious",
    "harmony", "hesitate", "humble", "incredible", "journey",
    "knowledge", "liberty", "magnificent", "marvelous", "mystery",
    "nervous", "opinion", "peculiar", "precious", "quaint",
    "reliable", "remarkable", "scholarly", "sensible", "shimmer",
    "sincere", "splendid", "sturdy", "terrifying", "treasure",
    "triumph", "unique", "valuable", "victory", "wisdom",
    "wonder", "yesterday", "zealous", "gravity", "habitat",
    
    # --- The Expanded Collection (A-C) ---
    "abandon", "ability", "aboard", "absorb", "absurd", "academy", "accent", "accept", "access", "accident",
    "accord", "account", "accuse", "achieve", "acid", "acquire", "across", "act", "active", "actor",
    "actual", "adapt", "add", "adept", "adjust", "admire", "admit", "adopt", "adore", "adult",
    "advance", "advice", "advise", "aerial", "affair", "affect", "afford", "afraid", "after", "again",
    "against", "age", "agency", "agent", "agile", "agree", "agriculture", "ahead", "aid", "aim",
    "air", "aircraft", "alarm", "album", "alert", "alien", "alike", "alive", "all", "alley",
    "allow", "ally", "almost", "alone", "along", "aloud", "alphabet", "already", "alter", "although",
    "always", "amaze", "ambition", "among", "amount", "amuse", "analyze", "anchor", "anger", "angle",
    "angry", "animal", "ankle", "announce", "annoy", "annual", "answer", "ant", "anticipate", "anxiety",
    "anxious", "any", "apart", "apology", "appeal", "appear", "apple", "apply", "appoint", "approach",
    "approve", "arch", "arctic", "area", "argue", "arise", "arm", "army", "around", "arrange",
    "arrest", "arrive", "arrow", "art", "article", "artist", "ascend", "ash", "aside", "ask",
    "asleep", "aspect", "assault", "assert", "assess", "asset", "assign", "assist", "assume", "assure",
    "athlete", "atmosphere", "attach", "attack", "attempt", "attend", "attention", "attitude", "attract", "auction",
    "audience", "author", "authority", "auto", "autumn", "available", "avenue", "average", "avoid", "awake",
    "award", "aware", "away", "awful", "awkward", "baby", "back", "background", "bacteria", "bad",
    "badge", "baffle", "bag", "bake", "balance", "ball", "balloon", "ban", "band", "bang",
    "bank", "banner", "bar", "bare", "bargain", "bark", "barn", "barrel", "barrier", "base",
    "basic", "basin", "basis", "basket", "bat", "bath", "battle", "bay", "beach", "beak",
    "beam", "bean", "bear", "beard", "beast", "beat", "beauty", "become", "bed", "bedroom",
    "bee", "beef", "before", "beg", "begin", "behave", "behavior", "behind", "being", "belief",
    "believe", "bell", "belong", "below", "belt", "bench", "bend", "beneath", "benefit", "berry",
    "beside", "best", "bet", "better", "between", "beyond", "bias", "bicycle", "big", "bike",
    "bill", "bind", "biology", "bird", "birth", "bit", "bite", "bitter", "black", "blade",
    "blame", "blank", "blanket", "blast", "blaze", "blend", "bless", "blind", "blink", "block",
    "blond", "blood", "bloom", "blow", "blue", "board", "boast", "boat", "body", "boil",
    "bold", "bolt", "bomb", "bond", "bone", "book", "boom", "boot", "border", "bore",
    "borrow", "boss", "both", "bother", "bottle", "bottom", "bounce", "bound", "bow", "bowl",
    "box", "boy", "brain", "brake", "branch", "brand", "brave", "bread", "break", "breakfast",
    "breath", "breathe", "breeze", "brick", "bridge", "brief", "bright", "bring", "broad", "broadcast",
    "brother", "brown", "brush", "bubble", "bucket", "budget", "buffalo", "bug", "build", "bulb",
    "bulk", "bull", "bullet", "bunch", "bundle", "burden", "burn", "burst", "bury", "bus",
    "bush", "business", "busy", "but", "butcher", "butter", "button", "buy", "buzz", "cabin",
    "cabinet", "cable", "cage", "cake", "calculate", "calendar", "call", "calm", "camera", "camp",
    "campaign", "can", "canal", "cancel", "candidate", "candle", "candy", "cannon", "canoe", "canvas",
    "canyon", "cap", "capable", "capacity", "capital", "captain", "capture", "car", "carbon", "card",
    "care", "career", "careful", "cargo", "carpet", "carriage", "carrot", "carry", "cart", "cartoon",
    "case", "cash", "cast", "castle", "cat", "catch", "category", "cattle", "cause", "caution",
    "cave", "cease", "ceiling", "celebrate", "cell", "cellar", "cement", "census", "center", "central",
    "century", "cereal", "ceremony", "certain", "chain", "chair", "challenge", "chamber", "champion", "chance",
    "change", "channel", "chaos", "chapter", "character", "charge", "charity", "charm", "chart", "chase",
    "chat", "cheap", "cheat", "check", "cheek", "cheer", "cheese", "chemical", "cherry", "chest",
    "chicken", "chief", "child", "chimney", "chin", "chip", "chocolate", "choice", "choose", "chop",
    "chorus", "chose", "church", "circle", "circus", "citizen", "city", "civil", "claim", "clam",
    "clap", "clarify", "class", "classic", "claw", "clay", "clean", "clear", "clerk", "clever",
    "click", "client", "cliff", "climate", "climb", "clinic", "clock", "close", "cloth", "cloud",
    "club", "clue", "coach", "coal", "coast", "coat", "code", "coffee", "coil", "coin",
    "cold", "collapse", "collar", "collect", "college", "colony", "color", "column", "comb", "combat",
    "combine", "come", "comedy", "comfort", "command", "comment", "commerce", "commit", "common", "communicate",
    "community", "company", "compare", "compass", "compel", "compete", "complain", "complete", "complex", "complicate",
    "compose", "compound", "concern", "concert", "conclude", "concrete", "condition", "conduct", "confess", "confuse",
    "connect", "conquer", "conscience", "consent", "consider", "consist", "constant", "construct", "contain", "content",
    "contest", "context", "continent", "continue", "contract", "contrast", "control", "convenient", "conversation", "convert",
    "convince", "cook", "cookie", "cool", "cooperate", "cop", "cope", "copper", "copy", "cord",
    "core", "corn", "corner", "correct", "cost", "costume", "cottage", "cotton", "couch", "cough",
    "council", "count", "counter", "country", "couple", "course", "court", "cover", "cow", "coward",
    "crack", "craft", "crash", "crawl", "crazy", "cream", "create", "creature", "credit", "creek",
    "creep", "crew", "crime", "criminal", "crisis", "crisp", "critic", "crop", "cross", "crow",
    "crowd", "crown", "cruel", "crush", "cry", "crystal", "cube", "culture", "cup", "cupboard",
    "cure", "curl", "current", "curtain", "curve", "cushion", "custom", "customer", "cut", "cycle",

    # --- D-H ---
    "dad", "daily", "dam", "damage", "damp", "dance", "danger", "dare", "dark", "data",
    "date", "daughter", "dawn", "day", "dead", "deaf", "deal", "dear", "debate", "debt",
    "decade", "decay", "deceive", "decide", "decision", "deck", "declare", "decline", "decorate", "decrease",
    "deep", "deer", "defeat", "defend", "define", "definite", "degree", "delay", "delight", "deliver",
    "demand", "democracy", "demonstrate", "den", "denim", "dense", "deny", "depart", "depend", "deposit",
    "depress", "depth", "derive", "descend", "describe", "desert", "deserve", "design", "desire", "desk",
    "despair", "despite", "destroy", "detail", "detect", "develop", "device", "devote", "dew", "dial",
    "diamond", "diary", "dictate", "dictionary", "die", "diet", "differ", "difficult", "dig", "digest",
    "dignity", "dim", "dime", "dine", "dinner", "dinosaur", "dip", "diplomat", "direct", "direction",
    "dirt", "disagree", "disappear", "disappoint", "disaster", "discipline", "discuss", "disease", "disgust", "dish",
    "dismiss", "display", "dispose", "distance", "distinct", "distribute", "district", "disturb", "ditch", "dive",
    "divide", "divine", "division", "divorce", "do", "dock", "doctor", "document", "dog", "doll",
    "dollar", "dolphin", "domain", "domestic", "dominate", "donkey", "door", "dot", "double", "doubt",
    "dough", "down", "doze", "draft", "drag", "dragon", "drain", "drama", "draw", "dread",
    "dream", "dress", "drift", "drill", "drink", "drive", "drop", "drown", "drug", "drum",
    "dry", "duck", "due", "dull", "dump", "dusk", "dust", "duty", "dwarf", "dwell",
    "eagle", "ear", "early", "earn", "earnest", "earth", "ease", "east", "easy", "eat",
    "ebb", "echo", "eclipse", "economy", "edge", "edit", "educate", "effect", "efficient", "effort",
    "egg", "eight", "either", "elaborate", "elastic", "elbow", "elder", "elect", "electric", "elegant",
    "element", "elephant", "elevate", "eleven", "elf", "eliminate", "elite", "else", "embarrass", "embassy",
    "embrace", "emerge", "emergency", "emotion", "emphasis", "empire", "employ", "empty", "enable", "enclose",
    "encounter", "encourage", "end", "endure", "enemy", "energy", "engage", "engine", "enjoy", "enlarge",
    "enough", "ensure", "enter", "entertain", "entire", "entrance", "entry", "envelope", "environment", "envy",
    "episode", "equal", "equip", "era", "erase", "errand", "error", "escape", "essay", "essential",
    "establish", "estate", "estimate", "eternal", "ethics", "evaporate", "even", "evening", "event", "ever",
    "every", "evidence", "evil", "exact", "exam", "examine", "example", "exceed", "excellent", "except",
    "exchange", "cite", "exclude", "excuse", "execute", "exercise", "exhaust", "exhibit", "exist", "exit",
    "expand", "expect", "expense", "expensive", "experience", "experiment", "expert", "explain", "explode", "explore",
    "export", "expose", "express", "extend", "exterior", "external", "extra", "extract", "extreme", "eye",
    "fabric", "face", "facility", "fact", "factor", "factory", "fade", "fail", "faint", "fair",
    "fairy", "faith", "fake", "fall", "false", "fame", "familiar", "family", "famine", "famous",
    "fan", "fancy", "far", "farm", "fashion", "fast", "fasten", "fat", "fatal", "fate",
    "father", "fatigue", "fault", "favor", "favorite", "fear", "feast", "feather", "feature", "federal",
    "fee", "feed", "feel", "fellow", "female", "fence", "ferry", "fertile", "festival", "fetch",
    "fever", "few", "fiber", "fiction", "field", "fierce", "fifteen", "fifth", "fifty", "fight",
    "figure", "file", "fill", "film", "filter", "final", "finance", "find", "fine", "finger",
    "finish", "fire", "firm", "first", "fish", "fist", "fit", "five", "fix", "flag",
    "flake", "flame", "flap", "flash", "flask", "flat", "flavor", "flaw", "flee", "fleet",
    "flesh", "flex", "flight", "float", "flock", "flood", "floor", "flour", "flow", "flower",
    "flu", "fluid", "flush", "fly", "foam", "focus", "fog", "foil", "fold", "folk",
    "follow", "food", "fool", "foot", "for", "forbid", "force", "forecast", "foreign", "forest",
    "forever", "forget", "forgive", "fork", "form", "formal", "format", "former", "fort", "fortune",
    "forty", "forum", "forward", "fossil", "found", "foundation", "fountain", "four", "fox", "fraction",
    "fragile", "fragment", "frame", "frank", "free", "freedom", "freeze", "frequency", "frequent", "fresh",
    "friend", "fright", "frog", "from", "front", "frost", "frown", "fruit", "frustrate", "fry",
    "fuel", "fulfill", "full", "fun", "function", "fund", "fundamental", "funeral", "funny", "fur",
    "furnish", "furniture", "further", "fury", "future", "gain", "galaxy", "gallery", "game", "gang",
    "gap", "garage", "garbage", "garden", "garlic", "gas", "gasp", "gate", "gather", "gauge",
    "gaze", "gear", "gem", "general", "generate", "generation", "genius", "gentle", "genuine", "geography",
    "germ", "gesture", "get", "ghost", "giant", "gift", "giggle", "giraffe", "girl", "give",
    "glad", "glance", "glare", "glass", "gleam", "glide", "glimpse", "globe", "gloom", "glory",
    "glove", "glow", "glue", "go", "goal", "goat", "god", "gold", "golf", "good",
    "goose", "gorge", "govern", "gown", "grace", "grade", "gradual", "graduate", "grain", "grammar",
    "grand", "grant", "grape", "graph", "grasp", "grass", "grateful", "grave", "gray", "grease",
    "great", "greed", "green", "greet", "grid", "grief", "grill", "grim", "grin", "grind",
    "grip", "groan", "grocery", "groom", "ground", "group", "grow", "growl", "growth", "guard",
    "guess", "guest", "guide", "guilt", "guitar", "gulf", "gum", "gun", "gym", "habit",
    "hail", "hair", "half", "hall", "halt", "hammer", "hand", "handle", "handsome", "hang",
    "happen", "happy", "harbor", "hard", "hardware", "harm", "harness", "harp", "harvest", "haste",
    "hat", "hatch", "hate", "haul", "haunt", "have", "hawk", "hazard", "haze", "head",
    "heal", "health", "heap", "hear", "heart", "heat", "heave", "heavy", "hedge", "heel",
    "height", "heir", "hello", "helmet", "help", "hen", "her", "herb", "herd", "here",
    "hero", "hide", "high", "hike", "hill", "hint", "hip", "hire", "history", "hit",
    "hive", "hobby", "hockey", "hold", "hole", "holiday", "hollow", "holy", "home", "honest",
    "honey", "honor", "hood", "hook", "hope", "horizon", "horn", "horror", "horse", "hospital",
    "host", "hot", "hotel", "hour", "house", "hover", "how", "howl", "hug", "huge",
    "hull", "human", "humid", "humor", "hunch", "hunger", "hunt", "hurdle", "hurricane", "hurry",
    "hurt", "husband", "hush", "hut", "hybrid", "hydrogen", "hygiene", "hymn", 
    
    # --- I-P ---
    "ice", "idea", "ideal", "identify", "idle", "idol", "ignore", "ill", "illegal", "illness",
    "illusion", "illustrate", "image", "imagine", "imitate", "immediate", "immense", "immigrant", "impact", "impair",
    "impatient", "implement", "imply", "import", "impose", "impossible", "impress", "improve", "impulse", "incident",
    "include", "income", "increase", "indeed", "index", "indicate", "individual", "industry", "inevitable", "infant",
    "infect", "infer", "inflate", "influence", "inform", "ingredient", "inhabit", "inherit", "initial", "inject",
    "injure", "ink", "inn", "innocent", "input", "inquire", "insect", "insert", "inside", "insight",
    "insist", "inspect", "inspire", "install", "instance", "instant", "instead", "instinct", "instruct", "instrument",
    "insult", "insurance", "intact", "integrate", "intellect", "intend", "intense", "intent", "interact", "interest",
    "interfere", "interior", "internal", "interpret", "interrupt", "interval", "interview", "into", "introduce", "invade",
    "invent", "invest", "investigate", "invite", "involve", "iron", "island", "isolate", "issue", "item",
    "ivory", "jacket", "jail", "jam", "jar", "jaw", "jazz", "jealous", "jeans", "jelly",
    "jet", "jewel", "job", "join", "joke", "jolly", "journal", "joy", "judge", "jug",
    "juice", "jump", "junction", "jungle", "junior", "junk", "jury", "just", "justice", "justify",
    "keen", "keep", "kettle", "key", "kick", "kid", "kidnap", "kidney", "kill", "kind",
    "king", "kingdom", "kiss", "kit", "kitchen", "kite", "kitten", "knee", "kneel", "knife",
    "knit", "knock", "knot", "know", "label", "labor", "laboratory", "lace", "lack", "ladder",
    "lady", "lake", "lamp", "land", "landscape", "lane", "language", "lantern", "lap", "large",
    "lark", "laser", "last", "late", "laugh", "launch", "laundry", "law", "lawn", "lawyer",
    "lay", "layer", "lazy", "lead", "leaf", "league", "leak", "lean", "leap", "learn",
    "least", "leather", "leave", "lecture", "left", "leg", "legal", "legend", "legislate", "lemon",
    "lend", "length", "lens", "leopard", "less", "lesson", "let", "letter", "level", "lever",
    "liar", "liberal", "library", "license", "lick", "lid", "lie", "life", "lift", "light",
    "lightning", "like", "limb", "lime", "limit", "limp", "line", "linen", "link", "lion",
    "lip", "liquid", "list", "listen", "literature", "little", "live", "load", "loaf", "loan",
    "lobby", "lobster", "local", "locate", "lock", "lodge", "log", "logic", "lonely", "long",
    "look", "loop", "loose", "lord", "lose", "loss", "lot", "loud", "love", "low",
    "loyal", "luck", "luggage", "lumber", "lump", "lunch", "lung", "lure", "luxury", "machine",
    "mad", "magazine", "magic", "magnet", "maid", "mail", "main", "maintain", "major", "make",
    "male", "mammal", "man", "manage", "mane", "manner", "mansion", "manual", "manufacture", "many",
    "map", "maple", "marble", "march", "margin", "marine", "mark", "market", "marriage", "marry",
    "marsh", "mart", "mask", "mass", "master", "mat", "match", "material", "math", "matter",
    "mature", "maximum", "may", "mayor", "maze", "meadow", "meal", "mean", "measure", "meat",
    "mechanic", "medal", "media", "medicine", "medium", "meet", "melt", "member", "memory", "mental",
    "mention", "menu", "merchant", "mercy", "mere", "merge", "merit", "merry", "mess", "message",
    "metal", "meter", "method", "metro", "microscope", "middle", "midnight", "might", "migrate", "mild",
    "mile", "military", "milk", "mill", "million", "mimic", "mind", "mine", "mineral", "minimum",
    "minister", "minor", "mint", "minute", "miracle", "mirror", "mischief", "miser", "miss", "missile",
    "mission", "mist", "mistake", "mix", "moan", "mob", "mobile", "mock", "mode", "model",
    "moderate", "modern", "modest", "modify", "moist", "mold", "mole", "moment", "monday", "money",
    "monitor", "monk", "monkey", "month", "mood", "moon", "moral", "more", "morning", "mortal",
    "mosquito", "moss", "most", "moth", "mother", "motion", "motive", "motor", "mount", "mountain",
    "mourn", "mouse", "mouth", "move", "movie", "much", "mud", "muffin", "mule", "multiply",
    "mumble", "municipal", "murder", "murmur", "muscle", "museum", "mushroom", "music", "must", "muster",
    "mutter", "mutual", "muzzle", "myth", "nail", "name", "nap", "napkin", "narrate", "narrow",
    "nasty", "nation", "native", "natural", "nature", "naval", "navigate", "navy", "near", "neat",
    "necessary", "neck", "need", "needle", "negative", "neglect", "negotiate", "neighbor", "neither", "nephew",
    "nerve", "nest", "net", "network", "neutral", "never", "new", "news", "next", "nice",
    "niche", "niece", "night", "nimble", "nine", "noble", "nobody", "nod", "noise", "nominate",
    "none", "noon", "normal", "north", "nose", "note", "nothing", "notice", "notify", "notion",
    "noun", "novel", "now", "nuclear", "number", "nurse", "nut", "nutrient", "oak", "oar",
    "oasis", "oath", "obedient", "obey", "object", "oblige", "observe", "obstacle", "obtain", "obvious",
    "occasion", "occupy", "occur", "ocean", "october", "odd", "odor", "off", "offend", "offer",
    "office", "officer", "official", "often", "oil", "old", "olive", "omen", "omit", "once",
    "onion", "only", "onset", "open", "opera", "operate", "oppose", "opposite", "opt", "optic",
    "optimism", "option", "oral", "orange", "orbit", "orchard", "orchestra", "order", "ordinary", "organ",
    "organic", "organize", "origin", "ornament", "orphan", "other", "ounce", "our", "out", "outcome",
    "outfit", "outlet", "outline", "output", "outrage", "outside", "oval", "oven", "over", "overcome",
    "owe", "owl", "own", "owner", "ox", "oxygen", "pace", "pack", "package", "packet",
    "pad", "paddle", "page", "pail", "pain", "paint", "pair", "palace", "pale", "palm",
    "pan", "panel", "panic", "pant", "paper", "parade", "paragraph", "parallel", "parcel", "pardon",
    "parent", "park", "parliament", "part", "participate", "particle", "particular", "partner", "party", "pass",
    "passage", "passenger", "passion", "passive", "passport", "past", "paste", "pasture", "pat", "patch",
    "path", "patience", "patient", "patrol", "patron", "pattern", "pause", "pave", "paw", "pay",
    "pea", "peace", "peak", "peanut", "pear", "pearl", "peasant", "pebble", "peck", "pedal",
    "peel", "peer", "peg", "pen", "penalty", "pencil", "pendulum", "penetrate", "penguin", "people",
    "pepper", "perceive", "percent", "perfect", "perform", "perfume", "perhaps", "period", "permanent", "permit",
    "persist", "person", "persuade", "pest", "pet", "petal", "phase", "philosophy", "phone", "photo",
    "phrase", "physical", "piano", "pick", "pickle", "picture", "pie", "piece", "pier", "pierce",
    "pig", "pigeon", "pile", "pilgrim", "pill", "pillar", "pillow", "pilot", "pin", "pinch",
    "pine", "pink", "pint", "pioneer", "pipe", "pirate", "pistol", "pit", "pitch", "pity",
    "pivot", "place", "plain", "plan", "plane", "planet", "plant", "plastic", "plate", "platform",
    "play", "player", "plea", "pleasant", "please", "pleasure", "pledge", "plenty", "plot", "plow",
    "pluck", "plug", "plunge", "plural", "plus", "pocket", "poem", "poet", "poetry", "point",
    "poison", "pole", "police", "policy", "polish", "polite", "politics", "poll", "pollen", "pond",
    "pony", "pool", "poor", "pop", "popular", "population", "porch", "pork", "port", "portion",
    "portrait", "pose", "position", "positive", "possess", "possible", "post", "pot", "potato", "potential",
    "pouch", "pound", "pour", "poverty", "powder", "power", "practice", "praise", "pray", "preach",
    "precede", "predict", "prefer", "prefix", "pregnant", "prejudice", "premier", "prepare", "presence", "present",
    "preserve", "president", "press", "pressure", "pretend", "pretty", "prevail", "prevent", "previous", "prey",
    "price", "pride", "priest", "primary", "prime", "primitive", "prince", "princess", "principal", "principle",
    "print", "prior", "prison", "private", "prize", "probable", "problem", "proceed", "process", "claim",
    "proclaim", "produce", "product", "profession", "profile", "profit", "program", "progress", "project", "prominent",
    "promise", "promote", "prompt", "pronoun", "pronounce", "proof", "propeller", "proper", "property", "prophet",
    "proportion", "propose", "prospect", "protect", "protest", "proud", "prove", "provide", "province", "provoke",
    "prudent", "psychology", "public", "publish", "puddle", "puff", "pull", "pulley", "pulp", "pulse",
    "pump", "pumpkin", "punch", "punctual", "punish", "pupil", "puppet", "puppy", "purchase", "pure",
    "purple", "purpose", "purse", "pursue", "push", "put", "puzzle", "pyramid",
    
    # --- Q-Z ---
    "quack", "quad", "quail", "quake", "qualify", "quality", "quantity", "quarrel", "quart", "quarter",
    "queen", "queer", "quest", "question", "quick", "quiet", "quilt", "quit", "quite", "quiz",
    "quote", "rabbit", "raccoon", "race", "rack", "racket", "radar", "radiant", "radio", "radish",
    "radius", "raft", "rag", "rage", "raid", "rail", "rain", "rainbow", "raise", "rake",
    "rally", "ram", "ranch", "random", "range", "rank", "rapid", "rare", "rascal", "rash",
    "rat", "rate", "rather", "ratio", "rattle", "raw", "ray", "razor", "reach", "react",
    "read", "ready", "real", "realize", "realm", "rear", "reason", "rebel", "recall", "receipt",
    "receive", "recent", "recipe", "recite", "reckless", "reckon", "recognize", "recommend", "record", "recover",
    "recruit", "rectangle", "red", "reduce", "reef", "reel", "refer", "referee", "reflect", "reform",
    "refuge", "refuse", "regard", "regime", "region", "register", "regret", "regular", "regulate", "reign",
    "rein", "reject", "relate", "relation", "relative", "relax", "release", "relevant", "relief", "religion",
    "rely", "remain", "remark", "remedy", "remember", "remind", "remote", "remove", "render", "rent",
    "repair", "repeat", "reply", "report", "represent", "republic", "reputation", "request", "require", "rescue",
    "research", "resemble", "resent", "reserve", "resident", "resist", "resolve", "resort", "resource", "respect",
    "respond", "response", "responsible", "rest", "restaurant", "restore", "restrict", "result", "retain", "retire",
    "retreat", "return", "reveal", "revenge", "reverse", "review", "revise", "revive", "revolt", "reward",
    "rhythm", "rib", "ribbon", "rice", "rich", "rid", "riddle", "ride", "ridge", "rifle",
    "right", "rigid", "rim", "ring", "riot", "rip", "ripe", "ripple", "rise", "risk",
    "ritual", "rival", "river", "road", "roar", "roast", "rob", "robe", "robin", "robot",
    "rock", "rocket", "rod", "role", "roll", "romance", "roof", "room", "root", "rope",
    "rose", "rot", "rotate", "rough", "round", "route", "routine", "row", "royal", "rub",
    "rubber", "rubbish", "rude", "rug", "ruin", "rule", "rumor", "run", "rural", "rush",
    "rust", "sack", "sacred", "sacrifice", "sad", "saddle", "safe", "safety", "sail", "saint",
    "sake", "salad", "salary", "sale", "salt", "salute", "same", "sample", "sand", "sandwich",
    "sane", "sash", "satellite", "satin", "satisfy", "sauce", "sausage", "savage", "save", "saw",
    "say", "scale", "scalp", "scan", "scandal", "scar", "scarce", "scare", "scarf", "scatter",
    "scene", "scent", "schedule", "scheme", "scholar", "school", "science", "scissors", "scold", "scoop",
    "scope", "score", "scorn", "scout", "scrape", "scratch", "scream", "screen", "screw", "script",
    "scrub", "sea", "seal", "search", "season", "seat", "second", "secret", "secretary", "section",
    "sector", "secure", "see", "seed", "seek", "seem", "segment", "seize", "seldom", "select",
    "self", "sell", "seminar", "senate", "send", "senior", "sense", "sensitive", "sentence", "separate",
    "september", "sequence", "series", "serious", "servant", "serve", "service", "session", "set", "settle",
    "seven", "several", "severe", "sew", "shade", "shadow", "shaft", "shake", "shall", "shallow",
    "shame", "shape", "share", "shark", "sharp", "shave", "she", "shear", "shed", "sheep",
    "sheer", "sheet", "shelf", "shell", "shelter", "sheriff", "shield", "shift", "shine", "ship",
    "shirt", "shiver", "shock", "shoe", "shoot", "shop", "shore", "short", "shot", "should",
    "shoulder", "shout", "shove", "show", "shower", "shred", "shrimp", "shrink", "shrub", "shrug",
    "shut", "shy", "sick", "side", "sidewalk", "siege", "sigh", "sight", "sign", "signal",
    "signature", "signify", "silence", "silent", "silk", "silly", "silver", "similar", "simple", "simulate",
    "sin", "since", "sing", "single", "sink", "sip", "sir", "siren", "sister", "sit",
    "site", "situation", "six", "size", "skate", "skeleton", "sketch", "ski", "skill", "skin",
    "skip", "skirt", "skull", "sky", "slab", "slack", "slam", "slap", "slash", "slate",
    "slave", "sled", "sleep", "sleeve", "slice", "slide", "slight", "slim", "slip", "slipper",
    "slit", "slogan", "slope", "slot", "slow", "slug", "slum", "slump", "sly", "small",
    "smart", "smash", "smell", "smile", "smoke", "smooth", "snack", "snail", "snake", "snap",
    "snare", "snarl", "snatch", "sneak", "sneeze", "sniff", "snow", "soak", "soap", "soar",
    "sob", "soccer", "social", "society", "sock", "soda", "sofa", "soft", "soil", "solar",
    "soldier", "sole", "solid", "solo", "solve", "some", "son", "song", "soon", "soothe",
    "sore", "sorrow", "sorry", "sort", "soul", "sound", "soup", "sour", "source", "south",
    "space", "spade", "spare", "spark", "sparrow", "speak", "spear", "special", "species", "specific",
    "specimen", "speech", "speed", "spell", "spend", "sphere", "spice", "spider", "spike", "spill",
    "spin", "spine", "spirit", "spit", "spite", "splash", "split", "spoil", "spoke", "sponge",
    "sponsor", "spoon", "sport", "spot", "spouse", "spray", "spread", "spring", "sprinkle", "spur",
    "spy", "squad", "square", "squash", "squat", "squeak", "squeeze", "squirrel", "stab", "stable",
    "stack", "stadium", "staff", "stage", "stain", "stair", "stake", "stale", "stalk", "stall",
    "stammer", "stamp", "stand", "standard", "star", "stare", "start", "starve", "state", "station",
    "statue", "status", "stay", "steady", "steak", "steal", "steam", "steel", "steep", "steer",
    "stem", "step", "stern", "stew", "stick", "sticky", "stiff", "still", "sting", "stir",
    "stitch", "stock", "stocking", "stomach", "stone", "stool", "stop", "store", "storm", "story",
    "stove", "straight", "strain", "strange", "strap", "straw", "streak", "stream", "street", "strength",
    "stress", "stretch", "strict", "stride", "strike", "string", "strip", "stripe", "strive", "stroke",
    "stroll", "strong", "structure", "struggle", "student", "studio", "study", "stuff", "stumble", "stump",
    "stupid", "style", "subject", "submarine", "submit", "substance", "substitute", "subtle", "subway", "succeed",
    "success", "such", "suck", "sudden", "suffer", "sugar", "suggest", "suit", "sum", "summer",
    "summit", "summon", "sun", "super", "supply", "support", "suppose", "suppress", "sure", "surface",
    "surge", "surgeon", "surplus", "surprise", "surrender", "surround", "survey", "survive", "suspect", "suspend",
    "swallow", "swamp", "swan", "swarm", "sway", "swear", "sweat", "sweater", "sweep", "sweet",
    "swell", "swift", "swim", "swing", "switch", "sword", "symbol", "sympathy", "symptom", "system",
    "table", "tackle", "tact", "tag", "tail", "tailor", "take", "tale", "talk", "tall",
    "tame", "tank", "tap", "tape", "tar", "target", "task", "taste", "tax", "taxi",
    "tea", "teach", "team", "tear", "tease", "technique", "technology", "telephone", "telescope", "television",
    "tell", "temper", "temperature", "temple", "temporary", "tempt", "ten", "tenant", "tend", "tender",
    "tennis", "tense", "tent", "term", "terminal", "terrace", "terrible", "territory", "terror", "test",
    "text", "texture", "than", "thank", "that", "thaw", "the", "theater", "theme", "then",
    "theory", "therapy", "there", "thermometer", "these", "thick", "thief", "thigh", "thin", "thing",
    "think", "thirst", "this", "thorn", "thorough", "those", "though", "thought", "thread", "threat",
    "threaten", "three", "threshold", "thrift", "thrill", "thrive", "throat", "throne", "throng", "through",
    "throw", "thrust", "thumb", "thunder", "thursday", "ticket", "tide", "tidy", "tie", "tiger",
    "tight", "tile", "till", "tilt", "timber", "time", "timid", "tin", "tiny", "tip",
    "tire", "tissue", "title", "to", "toad", "toast", "tobacco", "today", "toe", "together",
    "toilet", "token", "tolerate", "toll", "tomato", "tomorrow", "ton", "tone", "tongue", "tonight",
    "too", "tool", "tooth", "top", "topic", "torch", "tornado", "tortoise", "toss", "total",
    "touch", "tough", "tour", "tow", "toward", "towel", "tower", "town", "toy", "trace",
    "track", "tractor", "trade", "traffic", "tragedy", "trail", "train", "trait", "tramp", "transfer",
    "transform", "translate", "transmit", "transparent", "transport", "trap", "trash", "travel", "tray", "treat",
    "treaty", "tree", "tremble", "trend", "trial", "tribe", "trick", "trim", "trip", "troop",
    "trophy", "trouble", "trousers", "truck", "true", "trumpet", "trunk", "trust", "truth", "try",
    "tube", "tuesday", "tug", "tuition", "tulip", "tumble", "tune", "tunnel", "turkey", "turn",
    "turtle", "tutor", "twelve", "twenty", "twice", "twig", "twin", "twist", "two", "type",
    "typical", "tyrant", "ugly", "ulcer", "ultimate", "umbrella", "unable", "uncle", "under", "undergo",
    "understand", "undertake", "undo", "uneasy", "unemployment", "unfair", "unfold", "unfortunate", "unhappy", "uniform",
    "union", "unit", "unite", "universe", "university", "unknown", "unless", "until", "unusual", "up",
    "update", "upon", "upper", "upset", "upward", "urban", "urge", "urgent", "use", "used",
    "useful", "user", "usual", "utmost", "utter", "vacant", "vacation", "vacuum", "vague", "vain",
    "valley", "value", "valve", "van", "vanish", "vapor", "variable", "variety", "various", "vary",
    "vase", "vast", "vegetable", "vehicle", "veil", "vein", "velocity", "velvet", "venture", "verb",
    "verdict", "verify", "verse", "version", "vertical", "very", "vessel", "vest", "veteran", "veto",
    "vex", "via", "vibrate", "vice", "victim", "victor", "video", "view", "vigor", "vile",
    "village", "vine", "violate", "violence", "violet", "violin", "virtual", "virtue", "virus", "visible",
    "vision", "visit", "visual", "vital", "vitamin", "vivid", "vocabulary", "voice", "volcano", "volley",
    "volume", "voluntary", "volunteer", "vote", "vow", "vowel", "voyage", "vulgar", "wage", "wagon",
    "waist", "wait", "waiter", "wake", "walk", "wall", "wallet", "wander", "want", "war",
    "ward", "warm", "warn", "warrant", "wash", "waste", "watch", "water", "wave", "wax",
    "way", "we", "weak", "wealth", "weapon", "wear", "weather", "weave", "web", "wedding",
    "wedge", "weed", "week", "weep", "weigh", "weight", "weird", "welcome", "welfare", "well",
    "west", "wet", "whale", "what", "wheat", "wheel", "when", "where", "whether", "which",
    "while", "whip", "whisper", "whistle", "white", "who", "whole", "whom", "whose", "why",
    "wicked", "wide", "widow", "width", "wife", "wild", "will", "willow", "win", "wind",
    "window", "wine", "wing", "wink", "winner", "winter", "wipe", "wire", "wise", "wish",
    "wit", "witch", "with", "withdraw", "within", "without", "witness", "wolf", "woman", "wood",
    "wool", "word", "work", "world", "worm", "worry", "worse", "worship", "worst", "worth",
    "wound", "wrap", "wreck", "wrestle", "wrist", "write", "wrong", "yard", "yarn", "year",
    "yell", "yellow", "yes", "yet", "yield", "yolk", "young", "youth", "zebra", "zero",
    "zone", "zoo", "zoology", "zoom"
]


def generate_worksheet():
    # Ensure we have enough words to choose from
    if len(word_list) < 10:
        print("Error: The word list needs at least 10 words.")
        return

    # Randomly select 10 unique words
    selected_words = random.sample(word_list, 10)
    
    # Sort them alphabetically to make it easier to follow (optional)
    selected_words.sort()

    # ---------------------------------------------------------
    # 2. GENERATE HTML CONTENT
    # We use CSS to make lines for writing.
    # ---------------------------------------------------------
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Vocabulary Worksheet</title>
        <style>
            body {{
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                max-width: 850px;
                margin: 0 auto;
                padding: 40px;
                color: #333;
            }}
            h1 {{
                text-align: center;
                text-transform: uppercase;
                border-bottom: 2px solid #333;
                padding-bottom: 10px;
            }}
            .instructions {{
                text-align: center;
                font-style: italic;
                margin-bottom: 40px;
            }}
            .word-container {{
                margin-bottom: 25px;
                page-break-inside: avoid; /* Keeps word and lines together when printing */
            }}
            .word {{
                font-size: 22px;
                font-weight: bold;
                margin-bottom: 5px;
            }}
            .definition-lines {{
                width: 100%;
                height: 30px;
                border-bottom: 1px solid #000;
                margin-top: 15px;
            }}
            /* Print adjustments */
            @media print {{
                body {{ padding: 0; margin: 2cm; }}
                .no-print {{ display: none; }}
            }}
        </style>
    </head>
    <body>
        <h1>Dictionary Challenge</h1>
        <p class="instructions">Look up the following words in your dictionary and write the definitions on the lines provided.</p>
        
        <div class="worksheet">
    """

    # Create a block for each word
    for word in selected_words:
        html_content += f"""
            <div class="word-container">
                <div class="word">{word.capitalize()}</div>
                <!-- Two lines for writing -->
                <div class="definition-lines"></div>
                <div class="definition-lines"></div>
            </div>
        """

    html_content += """
        </div>
        <script>
            // Automatically bring up the print dialog when opened (optional)
            // window.print(); 
        </script>
    </body>
    </html>
    """

    # ---------------------------------------------------------
    # 3. SAVE AND OPEN THE FILE
    # ---------------------------------------------------------
    file_name = "daily_vocab.html"
    
    with open(file_name, "w") as f:
        f.write(html_content)
    
    print(f"Success! {file_name} has been created.")
    
    # Automatically open the file in the default web browser
    try:
        webbrowser.open('file://' + os.path.realpath(file_name))
    except:
        print(f"Could not auto-open browser. Please open {file_name} manually.")

if __name__ == "__main__":
    generate_worksheet()
