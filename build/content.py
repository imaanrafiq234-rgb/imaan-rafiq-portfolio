# -*- coding: utf-8 -*-
"""Content model for Imaan Rafiq's design portfolio.

All copy is sourced from the reference material supplied by the client
(LinkedIn project write-ups, the printed design portfolio deck, and the
Figma/Canva project links). All imagery is the client's own work.
"""

SITE = {
    "name": "Imaan Rafiq",
    "role": "Product & Industrial Designer",
    "discipline": "Design Engineering · CAD · Prototyping · UX",
    "email": "imaanrafiq234@gmail.com",
    "phone": "07392812939",
    "linkedin": "https://uk.linkedin.com/in/imaanrafiq",
    "location": "United Kingdom",
    # Set via the SITE_URL env var when building, e.g. SITE_URL=https://example.com
    "url": "",
    "intro": "Product Design & Technology graduate from Aston University, designing "
             "considered products that work for the people who use them.",
}

# tags used by the work-page filter
TAGS = [
    ("all", "Everything"),
    ("product", "Product design"),
    ("engineering", "Design engineering"),
    ("ux", "UX / UI"),
    ("sketch", "Sketch & form"),
    ("hardware", "Electronics"),
]

# Hero backdrop — a landscape plate with enough contrast to survive the overlay.
HERO_IMAGE = "coffee-machine/04.jpg"
HERO_FALLBACK = "smartwalker/00.jpg"

# --------------------------------------------------------------------------
# Case studies, in narrative order (flagship -> exploratory)
# --------------------------------------------------------------------------
PROJECTS = [
    {
        "slug": "smartwalker",
        "title": "SmartWalker",
        "subtitle": "Enhancing independent mobility",
        "category": "Final year project",
        "year": "2025",
        "tags": "product engineering hardware",
        "roles": "User research · CAD · Electronics · FEA · BOM costing",
        "tools": "SOLIDWORKS · ESP32-S3 · Arduino / C++ · KeyShot",
        "award": "James Dyson Award 2026 entry",
        "cover": "smartwalker/00.jpg",
        "summary": "An intelligent rollator that monitors posture, detects obstacles, "
                   "analyses gait and calls for help if the user falls — designed to be "
                   "affordable as well as clever.",
        "intro": [
            "Conventional mobility aids are often visually clinical, uncomfortable and "
            "technologically outdated, which contributes to reduced confidence, social "
            "stigma and limited independence for elderly users. The SmartWalker started "
            "as a simple question: what if a mobility aid actually worked for the person "
            "using it? Not just something to lean on, but something intelligent.",
            "I built the working prototype from scratch — user research, mechanical CAD, "
            "electronics, sensor fusion, FEA validation, a commercial BOM and a 12-section "
            "technical report. It has since been submitted to the 2026 James Dyson Award.",
        ],
        "sections": [
            {
                "title": "The problem",
                "body": [
                    "Conventional mobility aids are visually clinical, uncomfortable and "
                    "technologically outdated — contributing to reduced confidence, social "
                    "stigma and limited independence for elderly users.",
                ],
            },
            {
                "title": "The solution",
                "body": [
                    "A reimagined walker that combines ergonomic form with integrated smart "
                    "technology: posture monitoring, obstacle detection, AI-assisted gait "
                    "analysis, and emergency alerting — all in a lightweight, elegant package.",
                ],
            },
            {
                "title": "Engineering the intelligence",
                "body": [
                    "The firmware graduated from a basic benchtop test on an Arduino Uno to a "
                    "production-ready ESP32-S3. The 8-bit Uno proved the core logic, but "
                    "crunching sensor fusion across multiple I2C devices pushed it to its limit.",
                    "Moving to the 32-bit dual-core chip changed the game. High-frequency IMU "
                    "polling could be offloaded to one core while emergency braking and buzzer "
                    "logic stayed entirely on the other, with real multithreading and far more "
                    "headroom for advanced filtering.",
                ],
                "bullets": [
                    "LiDAR and ultrasonic obstacle detection",
                    "IMU-based posture and fall monitoring",
                    "AI-assisted gait analysis",
                    "Bluetooth / 4G emergency alerting with SMS",
                    "Haptic and audio feedback",
                    "Hybrid regenerative wheels assist braking and walking over uneven ground",
                ],
            },
            {
                "title": "Designed for more than one income",
                "body": [
                    "One thing I felt strongly about from the start: this should not be a "
                    "product only wealthy people can access. Mobility issues do not discriminate "
                    "by income, so the design split into two concepts.",
                    "The premium tier includes hybrid regenerative wheels that assist braking and "
                    "walking over uneven ground. The affordable tier strips back to the core "
                    "safety technology — fall detection, obstacle awareness, emergency alerts — "
                    "so the people who need it most can actually get it.",
                    "I believe it is ethically wrong to design assistive technology for one "
                    "sector of society and ignore everyone else.",
                ],
            },
            {
                "title": "Outcome",
                "body": [
                    "The walker supports users up to 130 kg, maintains a total weight below "
                    "6.5 kg, and allows continuous operation for 8 hours per battery cycle. "
                    "Electronics and sensor modules were packaged carefully to provide real-time "
                    "posture monitoring without significantly increasing weight.",
                ],
            },
        ],
        "gallery": [
            ("smartwalker/01.jpg", "SmartWalker — enhancing mobility: problem and solution"),
            ("smartwalker/00.jpg", "Project title and concept overview"),
            ("smartwalker/03.jpg", "Future of SmartWalker — healthcare mobility specification"),
            ("smartwalker/05.jpg", "Inspiration and moodboard"),
            ("smartwalker/06.jpg", "Company position — about us, clients, mission and vision"),
            ("smartwalker/02.jpg", "Arduino IoT build, emergency button and connection mapping"),
            ("smartwalker/04.jpg", "Smart assist, uphill braking control and contact"),
        ],
        "stats": [
            ("130 kg", "Maximum user weight"),
            ("6.5 kg", "Total system weight"),
            ("8 hrs", "Operation per battery cycle"),
            ("£252.99", "Target BOM cost"),
        ],
    },
    {
        "slug": "loom",
        "title": "LOOM",
        "subtitle": "End-to-end e-commerce UX/UI",
        "category": "Digital product design",
        "year": "2025",
        "tags": "ux product",
        "roles": "UX research · User journey mapping · UI design · Prototyping",
        "tools": "Figma · Auto Layout · Component libraries · Variants",
        "cover": "loom/00.jpg",
        "summary": "A fully functioning e-commerce experience for considered wardrobe and "
                   "home goods — built as a sandbox to show the complete UX and UI process.",
        "intro": [
            "I used to waste days trying to make initial designs perfect. Then I realised "
            "overthinking the first step just kills momentum.",
            "To sharpen my product design skills I created LOOM. While it is a fully "
            "functioning e-commerce site, it served as a sandbox to showcase my end-to-end "
            "UX/UI process — taking a rough concept and turning it into a user-tested interface.",
        ],
        "sections": [
            {
                "title": "Mapping the flow",
                "body": [
                    "The first slide is a low-fidelity six-step customer journey: browse, "
                    "evaluate, add to basket, checkout, confirm and thank you. Plotting it "
                    "rough and early meant friction points surfaced before any visual design "
                    "had been committed to.",
                ],
            },
            {
                "title": "High-fidelity UI",
                "body": [
                    "From the flow I moved into a full interface: dynamic product grids, "
                    "wishlist triggers, and clear category badges for Tops, Trousers, "
                    "Outerwear and Knitwear. Product cards carry price, imagery and "
                    "collection labels without crowding the grid.",
                    "The brand voice leans editorial — 'Made for the long way around', "
                    "'A considered wardrobe and home, for wherever the day takes you' — "
                    "so the layout gives typography room to breathe.",
                ],
            },
            {
                "title": "Figma workflow",
                "body": [
                    "The whole system was built with Auto Layout, component libraries and "
                    "variants for total scalability. Every screen is assembled from reusable "
                    "components, so new product categories or states can be introduced "
                    "without redrawing the interface.",
                ],
            },
        ],
        "gallery": [
            ("loom/00.jpg", "Customer journey — desktop, six-step flow"),
            ("loom/02.jpg", "Curated product grid — Wide-Leg Twill Trousers"),
            ("loom/03.jpg", "New arrivals and hover states across the product grid"),
            ("loom/04.jpg", "Editorial brand moment — 'Made for the long way around'"),
            ("loom/05.jpg", "Footer, journal and store navigation"),
            ("loom/01.jpg", "LOOM identity"),
        ],
        "stats": [
            ("6 steps", "Customer journey mapped"),
            ("4", "Product categories"),
            ("Auto Layout", "Fully componentised in Figma"),
        ],
    },
    {
        "slug": "nova-ledger",
        "title": "Nova Ledger",
        "subtitle": "Financial clarity, elevated",
        "category": "Visual & product design",
        "year": "2025",
        "tags": "ux product sketch",
        "roles": "Visual design · Typography · Layout · Dark-mode UI",
        "tools": "Figma · Display typography · Component variants",
        "cover": "nova-ledger/01.jpg",
        "summary": "A dark-mode concept advertisement carousel for a personal finance "
                   "platform — a weekend sprint in layout, typography and colour logic.",
        "intro": [
            "I spent a weekend playing around with layout, typography, and dark-mode UI. "
            "I wanted to challenge myself to take a screen usually crammed with numbers and "
            "make it feel clean, calm, and actually pleasant to look at.",
            "So I put together a concept advertisement carousel for a project I named "
            "NOVA Ledger. Instead of focusing on the tech behind it, I used this as a "
            "playground to sharpen my visual design skills.",
        ],
        "sections": [
            {
                "title": "Creating room to breathe",
                "body": [
                    "Stacking the headline and body text on the left while framing the visual "
                    "cards on the right gives your eyes a clear, comfortable path to follow. "
                    "The asymmetry is deliberate: text anchors, product floats.",
                ],
            },
            {
                "title": "Typographic hierarchy",
                "body": [
                    "Pairing a super bold display face with a simple body font makes sure your "
                    "brain instantly knows where to look first. Headlines do the shouting; "
                    "the supporting copy stays quiet and legible.",
                ],
            },
            {
                "title": "Colour logic",
                "body": [
                    "I went with a deep forest-green canvas to keep things easy on the eyes, "
                    "saving bright lime green only for the metrics and buttons that need to "
                    "stand out. The accent becomes a signal rather than decoration.",
                ],
            },
            {
                "title": "Subtle depth",
                "body": [
                    "Soft drop shadows, card overlays and rounded corners make the floating UI "
                    "elements feel tactile and modern — the interface reads as physical objects "
                    "resting on a surface rather than flat rectangles.",
                ],
            },
        ],
        "gallery": [
            ("nova-ledger/00.jpg", "NOVA Ledger identity"),
            ("nova-ledger/01.jpg", "Money, without the noise — hero and dashboard"),
            ("nova-ledger/02.jpg", "One view for every account — multi-account dashboard"),
            ("nova-ledger/03.jpg", "Clarity. Control. Confidence."),
            ("nova-ledger/04.jpg", "Insights that actually help — cash flow overview"),
            ("nova-ledger/05.jpg", "Your money, your momentum — habit and goal tracking"),
            ("nova-ledger/06.jpg", "Start with Nova Ledger — closing frame"),
        ],
        "stats": [
            ("7", "Carousel frames designed"),
            ("1 weekend", "Design sprint duration"),
            ("3", "Type scales in the hierarchy"),
        ],
    },
    {
        "slug": "coffee-machine",
        "title": "Cobra Coffee Machine",
        "subtitle": "Form, flow and internal architecture",
        "category": "Product design",
        "year": "2025",
        "tags": "product engineering sketch",
        "roles": "Research · Ideation · CAD modelling · Clay modelling",
        "tools": "SOLIDWORKS · KeyShot · Clay and card modelling",
        "cover": "coffee-machine/01.jpg",
        "summary": "A start-to-finish design development of a modern coffee machine, with a "
                   "design language drawn from the elegance and posture of a cobra.",
        "intro": [
            "The design language draws heavily from a sleek, organic, flowy aesthetic — "
            "specifically inspired by the elegance and posture of a cobra. The goal was to "
            "merge fluid movement with the clean, minimalist lines expected in high-end "
            "kitchen appliances.",
        ],
        "sections": [
            {
                "title": "The hidden challenge: internal layout",
                "body": [
                    "While the exterior silhouette often gets all the spotlight, one crucial "
                    "aspect of product design deserves far more recognition: the internal layout.",
                    "Fitting pumps, heating elements, water reservoirs and tubing into a dynamic, "
                    "tapered organic form is no easy feat. I am genuinely proud of how I tackled "
                    "and sorted out the internal architecture to ensure functionality does not "
                    "compromise form.",
                ],
            },
            {
                "title": "Visual direction",
                "body": [
                    "Visual direction is an important factor in order to fully understand and "
                    "communicate the design. Looking at typical coffee machines, I wanted my "
                    "design to reflect a strong connection to the home environment, focusing on "
                    "simplicity and a sense of nature.",
                    "To achieve this I incorporated tactility and warmth using soft edges and "
                    "smooth forms, and referenced the origins of coffee by integrating elements "
                    "inspired by coffee beans. A warm colour palette enhances the inviting, "
                    "natural feel. The visual direction was influenced by designers such as "
                    "Nendo and brands like Kikkoman, which emphasise minimalism and subtle "
                    "elegance. For the drip tray I took inspiration from Pikka, ensuring the "
                    "design is secure, stable and safe — with the machine accommodating a cup "
                    "seamlessly as part of the overall design.",
                ],
            },
            {
                "title": "Form analysis and layout study",
                "body": [
                    "Side and back views were analysed to test two competing architectures. "
                    "A tall layout suits a machine that is broad in a horizontal area rather "
                    "than vertical; a wide layout suits a machine that is compact in a short "
                    "vertical area rather than horizontal. Working both through on paper "
                    "settled the internal layout before any CAD time was spent.",
                ],
            },
            {
                "title": "Clay models and interface",
                "body": [
                    "Modelling a product — physically, in clay — is a key part of fixing "
                    "ergonomics and applying the user journey. I am glad to do this in every "
                    "product I assess; without it there is no kaizen.",
                    "Interface iterations improved access and user interaction, and the final "
                    "design fully integrates the water tank and makes clear how the machine "
                    "is operated.",
                ],
            },
            {
                "title": "Outcome",
                "body": [
                    "The final design gives the machine a cobra and hourglass look, which makes "
                    "it unique while staying modern and natural — meeting the design analysis "
                    "established by the form study. A selection of coffee options at the top of "
                    "the machine broadens the target customer and keeps them satisfied within "
                    "the design.",
                ],
            },
        ],
        "gallery": [
            ("coffee-machine/01.jpg", "Mechanism: once filled and switched on"),
            ("coffee-machine/00.jpg", "Concept development — initial form study"),
            ("coffee-machine/03.jpg", "Form analysis plate"),
            ("coffee-machine/04.jpg", "Side and back view internal layout development"),
            ("coffee-machine/05.jpg", "Visual direction statement"),
            ("coffee-machine/07.jpg", "Clay models — physical ergonomics study"),
            ("coffee-machine/06.jpg", "Process plate — form development"),
            ("coffee-machine/02.jpg", "Internal layout — pump, tank and tubing packaging"),
            ("coffee-machine/08.jpg", "Process plate — design development"),
            ("coffee-machine/c1.jpg", "Design exploration plate — cobra and hourglass silhouette, CMF palette, clay studies and thermal cutaway"),
        ],
        "stats": [
            ("3", "Development phases"),
            ("2", "Layout architectures tested"),
            ("1:1", "Clay model for ergonomics"),
        ],
    },
    {
        "slug": "pacifier",
        "title": "Cocomelon Pacifier",
        "subtitle": "Child safety, materials and circular economy",
        "category": "Product design",
        "year": "2025",
        "tags": "product engineering sketch",
        "roles": "Persona research · Concept sketching · Engineering drawings · Material study",
        "tools": "Injection moulding study · Silicone material research · 3D printed model",
        "cover": "pacifier/00.jpg",
        "summary": "A pacifier developed around a single-mum persona, where material choice "
                   "is not a styling decision — it is the whole product.",
        "intro": [
            "Anything that goes into a child's mouth carries a responsibility most products "
            "do not. Material choice is not a styling decision here; it is the whole product.",
            "I specified silicone plastic — heat resistant, water repellent and flexible, "
            "already trusted across children's products and medical devices in the UK. No "
            "harsh plastics, no toxic additives, nothing that risks a child's health for the "
            "sake of a lower unit cost.",
        ],
        "sections": [
            {
                "title": "Design considerations",
                "body": [
                    "The concept was designed around real pacifier problems, not just the look "
                    "of the product.",
                ],
                "bullets": [
                    "Dependency — some babies become overly dependent, making weaning hard. "
                    "Adding a teether lets the baby reduce pain and slowly come off it.",
                    "Nipple confusion — introducing a pacifier too early can make latching "
                    "difficult, so a suitable age range has to be considered.",
                    "Sleep disruption — a pacifier can become a sleep association, so if it "
                    "falls out at night the baby wakes. This drives the soft, easily replaced form.",
                    "Hygiene — pacifiers accumulate dirt, saliva and bacteria, so the shell is "
                    "shaped for straightforward cleaning and sterilising.",
                ],
            },
            {
                "title": "United States point of difference",
                "body": [
                    "The Cocomelon-inspired shell has soft, distinguishable features so the "
                    "child recognises it and wants to use it. Colour choices are not random: "
                    "green for calm, cream for warmth and nostalgia, red to catch a parent's eye "
                    "on the shelf, and blue to signal trust and safety — colours already "
                    "associated with children's safety products in the UK.",
                    "A lip and groove construction lets the shell and mouthpiece assemble "
                    "cleanly for injection moulding, keeping the design manufacturable at scale.",
                    "Engineering drawings allow the product to be mass produced with sufficient "
                    "and exact results via injection moulding.",
                ],
            },
            {
                "title": "Material: silicone plastic",
                "body": [
                    "Silicone is a synthetic polymer of silicon, oxygen, carbon and hydrogen. "
                    "It is used in kitchen utensils, medical devices and sealants, and differs "
                    "from traditional plastics because it stays flexible and heat resistant.",
                    "It cannot be easily recycled — it undergoes complex methods including "
                    "melting and reshaping, typically broken down or ground into a powder, and "
                    "can be reused as a filler for other products. Because it is not as "
                    "established as other plastics, silicone needs specialised machinery. "
                    "Cost sits around £2–£10 depending on the retailer and design.",
                ],
            },
            {
                "title": "Wastage and the circular economy",
                "body": [
                    "Wastage and the circular economy were just as important as safety. Silicone "
                    "is not the easiest material to recycle, but it holds up to repeated "
                    "sterilising and reuse far longer than cheaper alternatives, which cuts down "
                    "how often a parent needs to replace it.",
                    "I chose this design because I believe it best aids the future generation "
                    "into a circular economy — the mothers who need these pacifiers will buy "
                    "them and recommend them, and the product can be injection moulded at ease "
                    "and mass produced with intricate detail if needed.",
                ],
            },
        ],
        "gallery": [
            ("pacifier/00.jpg", "Final concept — 3D printed silicone pacifier"),
            ("pacifier/01.jpg", "Design considerations: dependency, nipple confusion, sleep, hygiene"),
            ("pacifier/04.jpg", "Concept iteration — pacifier form sketches"),
            ("pacifier/02.jpg", "Engineering drawings for injection moulding"),
            ("pacifier/03.jpg", "Material consideration — silicone plastic"),
            ("pacifier/05.jpg", "Reasoning for the final design and colour logic"),
        ],
        "stats": [
            ("4", "Core user problems addressed"),
            ("5", "Colours with defined meaning"),
            ("Silicone", "Specified for safety and reuse"),
        ],
    },
    {
        "slug": "rugged-speaker",
        "title": "Rugged Speaker",
        "subtitle": "Where the design journey started",
        "category": "First university project",
        "year": "2023",
        "tags": "product sketch",
        "roles": "Research · Data collection · Form analysis · Concept design · CAD",
        "tools": "SOLIDWORKS · KeyShot · Sketching",
        "cover": "rugged-speaker/13.jpg",
        "summary": "My very first university design project — revisiting it shows how a simple "
                   "geometric form becomes a considered design feature through structured iteration.",
        "intro": [
            "Revisiting my very first university design project has been a valuable reminder "
            "of how far my skills and design thinking have progressed — and how much my early "
            "designs relied on enthusiasm rather than refinement.",
            "The brief focused on designing a rugged speaker, requiring a balance between "
            "durability, functionality and visual appeal. The process reinforced the "
            "importance of research, data collection and form analysis in guiding design "
            "decisions.",
        ],
        "sections": [
            {
                "title": "Process",
                "body": [
                    "I explored different shapes and materials, then iterated the design to "
                    "improve the clay model, the internal layout, the render and the overall form. "
                    "Initial sketches drove the shape; the physical model validated how it sat "
                    "in the hand.",
                ],
            },
            {
                "title": "Accessibility and protection",
                "body": [
                    "Port placement was a deliberate decision: making the ports accessible and "
                    "obtainable while reducing the risk of the speaker getting damaged. The "
                    "final design presents the USB ports and charging port clearly on the body.",
                ],
            },
            {
                "title": "Reflection",
                "body": [
                    "Alongside traditional design methods, AI has since become a valuable tool "
                    "in my workflow — supporting ideation, exploration and efficiency while "
                    "keeping human creativity and judgement at the core.",
                    "Looking back: a sleek, modern form; compact and portable; designed for "
                    "everyday use; a strong aesthetic focus, though the technical detailing "
                    "could go further. This project is where I developed form and styling skills.",
                ],
            },
        ],
        "gallery": [
            ("rugged-speaker/03.jpg", "Design idea chosen"),
            ("rugged-speaker/13.jpg", "Actual speaker design"),
            ("rugged-speaker/14.jpg", "USB ports and charging port"),
            ("rugged-speaker/06.jpg", "Durability, accessibility and protection reasoning"),
            ("rugged-speaker/00.jpg", "Concept development sheet"),
            ("rugged-speaker/01.jpg", "Ideation and form exploration"),
            ("rugged-speaker/02.jpg", "Sketch range"),
            ("rugged-speaker/04.jpg", "Sketch study"),
            ("rugged-speaker/05.jpg", "Sketch study"),
            ("rugged-speaker/07.jpg", "Form development"),
            ("rugged-speaker/08.jpg", "Form development"),
            ("rugged-speaker/09.jpg", "Model and layout study"),
            ("rugged-speaker/10.jpg", "Iteration plate"),
            ("rugged-speaker/11.jpg", "Iteration plate"),
            ("rugged-speaker/12.jpg", "Final render development"),
        ],
        "stats": [
            ("2023", "First university project"),
            ("4", "Iteration stages"),
            ("1", "Clay model built"),
        ],
    },
    {
        "slug": "prosthetic-hand",
        "title": "Prosthetic Hand",
        "subtitle": "Designed around how a chef actually works",
        "category": "Design engineering",
        "year": "2025",
        "tags": "engineering hardware sketch",
        "roles": "Form and concept analysis · Technical sketching · Electronics build",
        "tools": "Arduino Uno · Flex sensor · Servo motors · Silicone dome",
        "cover": "prosthetic-hand/00.jpg",
        "summary": "A prosthetic hand for use in a professional kitchen — built from a study of "
                   "how a hand actually grips, holds and manipulates a knife.",
        "intro": [
            "Continuing the sketching series — this time a prosthetic hand designed for use in "
            "a kitchen environment.",
            "The early sketches started with form and concept analysis, studying how a hand "
            "actually grips, holds and manipulates a knife or utensil. A prosthetic hand for "
            "a chef has to move the way a working hand moves, not just look like one.",
        ],
        "sections": [
            {
                "title": "From sketches to constraints",
                "body": [
                    "From there the sketches got more technical. I annotated where the circuit "
                    "could sit on top of the prosthetic arm rather than the palm, since that is "
                    "the surface a chef uses constantly and the electronics would be damaged.",
                    "I worked out how many motion pins the fingers needed, and flagged early that "
                    "the strings pulling the fingers had to be robust enough not to get "
                    "accidentally cut by a knife mid-use. Even the aesthetic of the wiring got "
                    "sketched out — not flashy, blending into a professional kitchen environment "
                    "rather than standing out.",
                    "One sketch pushed the concept further with a seasoning dispenser built into "
                    "the fingers, pouring straight into a shot measure — designed specifically "
                    "around how a chef works, not just a generic hand replacement.",
                ],
            },
            {
                "title": "The build",
                "body": [
                    "A flex sensor attached to the user's arm reads movement and sends the "
                    "coding to an Arduino board, which sends it into the servo motors pulling "
                    "the hand simulation — the same string and pulley logic from the early sketches.",
                    "A temperature sensor in the fingertips triggers an LED and vibration motor: "
                    "red for hot and blue for cold, so the user gets a warning before contact "
                    "with something dangerous. The arm itself sits inside a silicone dome for "
                    "protection.",
                ],
            },
            {
                "title": "Why the sketching stage mattered",
                "body": [
                    "None of that would have come together without the sketching stage first. "
                    "Every constraint — where the circuit goes, how the fingers move, what a "
                    "chef actually needs from their hand — got worked out on paper before a "
                    "single part was made.",
                ],
            },
        ],
        "gallery": [
            ("prosthetic-hand/01.jpg", "System logic — flex sensor to Arduino to servo motors"),
            ("prosthetic-hand/00.jpg", "Form analysis and grip study"),
            ("prosthetic-hand/02.jpg", "Technical development"),
            ("prosthetic-hand/03.jpg", "Concept and constraint sketching"),
            ("prosthetic-hand/04.jpg", "Annotated technical sketches"),
            ("prosthetic-hand/05.jpg", "Circuit placement and protection study"),
            ("prosthetic-hand/07.jpg", "Final build"),
            ("prosthetic-hand/06.jpg", "Final build detail"),
            ("prosthetic-hand/c1.jpg", "Mechatronics and sensing — flex sensor control loop, forearm cuff and thermal warning system"),
        ],
        "stats": [
            ("Red / blue", "Hot and cold haptic warning"),
            ("Arduino Uno", "Flex sensor to servo control"),
            ("1", "Seasoning dispenser concept"),
        ],
    },
    {
        "slug": "pump-system",
        "title": "Pump System",
        "subtitle": "The paper trail behind the product",
        "category": "Hardware engineering",
        "year": "2025",
        "tags": "engineering hardware sketch",
        "roles": "Systems design · Circuit design · Calculations · CAD",
        "tools": "Sketches · Block diagram · Circuit schematic · SOLIDWORKS",
        "cover": "pump-system/00.jpg",
        "summary": "A full engineering paper trail — geometry sketches, system block diagram, "
                   "circuit schematic, sizing calculations and CAD — for a pressure pump system.",
        "intro": [
            "Every line on paper carries a journey that pristine 3D renders often hide.",
            "Yes, my lines are not perfectly straight, my handwriting is questionable and the "
            "layout is not picture perfect. But this concept is where real engineering happens: "
            "tracing the life of an idea from the first spark to a fully realised product.",
        ],
        "sections": [
            {
                "title": "Step 1 — Physical intuition",
                "body": [
                    "Getting the raw pump geometry and fluid dynamics on paper: sizing the main "
                    "cylinder, wrestling with flow resistance — 'flow doesn't like corners' — "
                    "and defining how pressure transducer membranes turn mechanical movement "
                    "into electrical signals.",
                ],
            },
            {
                "title": "Step 2 — System logic",
                "body": [
                    "A block diagram mapping out the pump's brain: routing signal pathways from "
                    "voltage dividers and current sensors into op-amps to drive panel meters and "
                    "status LEDs.",
                ],
            },
            {
                "title": "Step 3 — Circuit design",
                "body": [
                    "Turning abstract logic into a working circuit, integrating 7-segment "
                    "displays, operational amplifiers and resistor networks to read 3-bar "
                    "pressure inputs.",
                ],
            },
            {
                "title": "Step 4 — Calculations and sizing",
                "body": [
                    "Validating reality against theory. Given 12 Vdc and a maximum current draw "
                    "of 10 A, maximum power consumption is 120 W; at a typical 2.5 A draw it is "
                    "30 W. Running continuously for one minute at 30 W uses 1800 J of energy.",
                    "This is less than the estimated input requirement calculated earlier, "
                    "indicating that either the pump must run longer or power input must be "
                    "higher during operation.",
                    "Component values were then sized: to scale 14 V down to 1.999 V, the "
                    "voltage divider ratio should be approximately 1:7 — a typical setup uses "
                    "R1 = 33 kΩ and R2 = 4.7 kΩ. The current-sensor amplifier needs a gain of "
                    "around 50, and the pressure-sensor amplifier needs a gain of 2.",
                ],
            },
            {
                "title": "Step 5 — CAD and production",
                "body": [
                    "Bringing all four layers together into a functional 3D CAD model.",
                    "A final product shows what was built, but the paper trail reveals why it "
                    "works. It captures the trial and error, the excessive problem-solving, and "
                    "the quiet beauty of bringing an idea into existence. Never hide your rough "
                    "drafts — they are the heartbeat of innovation.",
                ],
            },
        ],
        "gallery": [
            ("pump-system/00.jpg", "Geometry sketches — flow resistance and transducer membranes"),
            ("pump-system/01.jpg", "Block diagram — sensors, amps, panel meters and LEDs"),
            ("pump-system/02.jpg", "Circuit schematic"),
            ("pump-system/03.jpg", "Power and energy calculations"),
            ("pump-system/04.jpg", "Component values — voltage divider and amplifier gains"),
            ("pump-system/05.jpg", "CAD and production model"),
            ("pump-system/c1.jpg", "Electrical engineering — laminar flow geometry and the pressure transducer signal chain"),
        ],
        "stats": [
            ("120 W", "Maximum power draw"),
            ("30 W", "Typical power draw"),
            ("1800 J/min", "Measured energy consumption"),
            ("3 bar", "Pressure input range"),
        ],
    },
    {
        "slug": "breathalyser",
        "title": "Breathalyser",
        "subtitle": "Sketch, CAD, render",
        "category": "Product design",
        "year": "2024",
        "tags": "product engineering sketch",
        "roles": "Concept sketching · Parametric CAD · Final rendering",
        "tools": "SOLIDWORKS · KeyShot",
        "cover": "breathalyser/00.jpg",
        "summary": "A handheld alcohol breathalyser taken through the full pipeline — red-line "
                   "concepts, parametric CAD and a high-fidelity render.",
        "intro": [
            "As part of my ongoing series sharing design and form analysis two to three times "
            "a week, this is the complete evolution of a handheld alcohol breathalyser: "
            "ideation, engineering and presentation.",
        ],
        "sections": [
            {
                "title": "From form to envelope",
                "body": [
                    "The loose volumes explored in the early sketch phase were locked down to a "
                    "precise footprint in the CAD model — the absolute sweet spot for housing the "
                    "internal fuel-cell sensor block while keeping the device highly portable.",
                ],
            },
            {
                "title": "From lines to ergonomics",
                "body": [
                    "The organic curves from the sketch became an engineered reality. The handle "
                    "tapers down to a 28 mm depth, creating a natural contour that sits securely "
                    "in the user's palm.",
                ],
            },
            {
                "title": "Preserving the sight-line",
                "body": [
                    "To ensure a user can clearly read the screen while blowing into the unit, "
                    "the mouthpiece axis was engineered with a specific 15 mm offset from the top "
                    "casing. This perfectly maintains the 45° sight-line angle down to the "
                    "display screen.",
                ],
            },
            {
                "title": "Ready for production",
                "body": [
                    "In the final render you can see how the UI elements come together. The "
                    "screen pocket is optimised for a crisp, standard OLED display, paired with "
                    "tactically spaced buttons to prevent mispresses.",
                    "Taking a product all the way from a blank page to a realistic render is a "
                    "masterclass in compromise — finding where styling, engineering metrics and "
                    "user interaction meet seamlessly.",
                ],
            },
        ],
        "gallery": [
            ("breathalyser/00.jpg", "Red-line concept sketches — form, volume and layout"),
            ("breathalyser/01.jpg", "Parametric SolidWorks CAD model"),
            ("breathalyser/02.jpg", "High-fidelity final render"),
        ],
        "stats": [
            ("28 mm", "Handle depth at the palm"),
            ("15 mm", "Mouthpiece axis offset"),
            ("45°", "Maintained sight-line angle"),
        ],
    },
    {
        "slug": "professor-layton",
        "title": "Professor Layton Device",
        "subtitle": "World-building through form",
        "category": "Concept exercise",
        "year": "2024",
        "tags": "product sketch",
        "roles": "Visual DNA mapping · Form ideation · CAD · Physical prototype",
        "tools": "SOLIDWORKS · Physical model · Reference analysis",
        "cover": "professor-layton/03.jpg",
        "summary": "A real-world, tactile interpretation of a handheld communication device "
                   "inspired by Nintendo's Professor Layton — world-building through form.",
        "intro": [
            "Have you ever wondered what the technology from your favourite game worlds would "
            "feel like in the palm of your hand?",
            "I absolutely adored playing this game growing up — the animation style, the "
            "storytelling and the whimsical mechanics completely captivated me. Getting to "
            "deconstruct its visual universe as a designer has been brilliant.",
        ],
        "sections": [
            {
                "title": "The visual DNA",
                "body": [
                    "Mapping the design language: I pulled form cues directly from the game's "
                    "architecture and vehicles — turning arched windows into a speaker grille, "
                    "and clockwork gears into functional interface selectors.",
                ],
            },
            {
                "title": "Form ideation",
                "body": [
                    "Sketching multiple asymmetrical oval silhouettes to see how a stylised, "
                    "pebble-like chassis could comfortably drop into a real human palm.",
                ],
            },
            {
                "title": "The CAD breakdown",
                "body": [
                    "Moving the chosen form into 3D space to refine the physical proportions, "
                    "mechanical gear tolerances, and clean up the overall envelope.",
                ],
            },
            {
                "title": "Interaction and prototype",
                "body": [
                    "Mapping the user journey and testing the final, physical piece. Fictional "
                    "tech doesn't care about internal component constraints, but real hands do. "
                    "Forcing a whimsical shape to perfectly balance its weight and button spacing "
                    "for a natural, one-handed grip is a masterclass in ergonomics.",
                    "In a world dominated by flat glass touchscreens, this device relies entirely "
                    "on physical mechanics. The side dials turn to select 'communicators', and "
                    "the controls are purposefully spaced to encourage slow, deliberate engagement "
                    "rather than rapid tapping. It turns device interaction into a puzzle-solving "
                    "experience.",
                    "Fictional or not, great product design always comes down to asking: if this "
                    "existed in real life, how would it feel to hold, click and use?",
                ],
            },
        ],
        "gallery": [
            ("professor-layton/03.jpg", "Interactions and communication — control layout"),
            ("professor-layton/00.jpg", "Pebble-like asymmetric silhouette ideation"),
            ("professor-layton/01.jpg", "Form ideation sheet"),
            ("professor-layton/02.jpg", "CAD breakdown and envelope refinement"),
            ("professor-layton/04.jpg", "World-building narrative — Layton's garage"),
            ("professor-layton/c1.jpg", "Tactile mechanical prop — brass escapements, copper conduit routing and weighted rotary switches"),
        ],
        "stats": [
            ("4", "Design pipeline stages"),
            ("0", "Touchscreens — physical mechanics only"),
            ("2D → 3D", "Reference page to physical model"),
        ],
    },
    {
        "slug": "audi-r8",
        "title": "Audi R8 Form Analysis",
        "subtitle": "Form is function",
        "category": "Automotive study",
        "year": "2025",
        "tags": "sketch",
        "roles": "Automotive sketching · Aerodynamic and proportion analysis",
        "tools": "Marker and pen sketching",
        "cover": "audi-r8/00.jpg",
        "summary": "A concept and form analysis of the Audi R8 — how pure performance shapes "
                   "every line on the page.",
        "intro": [
            "Great automotive design isn't drawn. It's calculated. Behind every icon like the "
            "Audi R8 is a constant battle between styling and physics.",
        ],
        "sections": [
            {
                "title": "Proportional stance",
                "body": [
                    "A mid-engine layout forces a cab-forward volume to perfectly balance axle "
                    "weight. The proportion is a consequence of where the mass has to sit.",
                ],
            },
            {
                "title": "Lighting architecture",
                "body": [
                    "Sharp DRL matrices define brand identity while framing front cooling ducts. "
                    "Lighting does aerodynamic work as well as brand work.",
                ],
            },
            {
                "title": "Aerodynamic taper",
                "body": [
                    "A Coke-bottle side profile channels clean airflow straight to the rear wing.",
                ],
            },
            {
                "title": "Surface tension",
                "body": [
                    "Concave flanks pull the bodywork tight to scoop high-pressure air into the "
                    "side blades. Form never merely follows function. Form is function.",
                ],
            },
        ],
        "gallery": [
            ("audi-r8/00.jpg", "Aerodynamics and side view — lighting signature and visual identity"),
            ("audi-r8/01.jpg", "Surface tension and side blade study"),
            ("audi-r8/02.jpg", "Proportional stance and coke-bottle profile"),
        ],
        "stats": [
            ("Mid-engine", "Layout driving the whole stance"),
            ("4", "Analysis principles applied"),
        ],
    },
    {
        "slug": "underwater-drone",
        "title": "Underwater Drone",
        "subtitle": "Golden Snitch inspired",
        "category": "Concept study",
        "year": "2024",
        "tags": "sketch product",
        "roles": "Concept sketching · Surface modelling · Model quality",
        "tools": "Sketching · SOLIDWORKS surface modelling",
        "cover": "underwater-drone/00.jpg",
        "summary": "Early-stage concept iterations for an underwater drone, inspired by the "
                   "Golden Snitch from Harry Potter.",
        "intro": [
            "The brief was to design a future robot to solve a problem or assist with a task, "
            "practising surface modelling and model quality.",
            "Here are a few initial iterations for an underwater drone design, heavily inspired "
            "by the Golden Snitch from Harry Potter. Nothing has to be perfect at this stage — "
            "just diving into some raw sketches and early ideation.",
        ],
        "sections": [
            {
                "title": "Research and insight",
                "body": [
                    "The concept was grounded in drowning and water safety, regenerative design, "
                    "existing drones on the market, and a form analysis of the golden snitch "
                    "silhouette — reconciling a playful form language with a serious safety function.",
                ],
            },
            {
                "title": "Process and outcome",
                "body": [
                    "From research through storyboarding to surface modelling, the project was an "
                    "exercise in form quality: how closely can an organic, spherical form be "
                    "controlled in CAD without losing the original sketch intent.",
                ],
            },
        ],
        "gallery": [
            ("underwater-drone/00.jpg", "Concept sketch — golden snitch form iterations"),
            ("underwater-drone/01.jpg", "Form development"),
            ("underwater-drone/02.jpg", "Form development"),
            ("underwater-drone/03.jpg", "Form development"),
        ],
        "stats": [
            ("Water safety", "Problem being solved"),
            ("Surface modelling", "Core skill practised"),
        ],
    },
    {
        "slug": "pizza-oven",
        "title": "Pizza Oven",
        "subtitle": "Sketch, mockup, render",
        "category": "Concept study",
        "year": "2025",
        "tags": "product sketch",
        "roles": "Concept sketching · Cardboard mockup · Material and finish intent",
        "tools": "Sketching · Card mockup · Rendering",
        "cover": "pizza-oven/00.jpg",
        "summary": "A pizza oven concept developed sketch-first, then proven in cardboard, then "
                   "refined in render.",
        "intro": [
            "Sketch first, or straight to CAD? I don't think there's a single right answer. "
            "For me it's usually where the early thinking happens — fast, rough, low commitment. "
            "That said, I go straight into 3D sometimes too, when I already know the form and "
            "just want to get it out before the idea moves.",
            "This one's a pizza oven concept, developed sketch first.",
        ],
        "sections": [
            {
                "title": "How it works",
                "body": [
                    "The chimney manages airflow so the oven doesn't overheat. Air holes let you "
                    "see the coal and the pizza, so you know it's cooking safely and evenly. The "
                    "coal loads and clears through a side hole using a shovel. The angled legs "
                    "give it stability and a bit of a modern edge over a traditional build.",
                ],
            },
            {
                "title": "Three stages, one idea",
                "body": [
                    "From there it went to a quick cardboard mockup to check proportions and form "
                    "in real space, then into a render to test material and finish intent — walnut "
                    "veneer body, white powder-coated ends, castors for mobility.",
                    "Three very different stages, same idea carried through each one.",
                ],
            },
        ],
        "gallery": [
            ("pizza-oven/00.jpg", "Annotated concept sketch — chimney, airflow and legs"),
            ("pizza-oven/01.jpg", "Cardboard mockup for proportion and form"),
            ("pizza-oven/02.jpg", "Material and finish render"),
        ],
        "stats": [
            ("3", "Stages: sketch, mockup, render"),
            ("Walnut veneer", "Body material intent"),
            ("Castors", "Mobility"),
        ],
    },
    {
        "slug": "embedded-systems",
        "title": "Embedded Systems Series",
        "subtitle": "Understanding the brain behind modern devices",
        "category": "Technical communication",
        "year": "2024",
        "tags": "hardware engineering",
        "roles": "Research · Technical writing · Visual explanation",
        "tools": "Adobe Illustrator · Technical diagrams",
        "cover": "embedded-systems/00.jpg",
        "summary": "A beginner's guide to embedded systems — block diagrams, component "
                   "comparisons and applications, written and drawn to be genuinely readable.",
        "intro": [
            "A specialised computer system designed to perform a specific task inside a larger "
            "device. This series breaks embedded systems down for people meeting them for the "
            "first time.",
        ],
        "sections": [
            {
                "title": "Key characteristics",
                "body": [
                    "Embedded systems share a set of defining traits: dedicated function, "
                    "real-time operation, low power consumption, reliable performance and "
                    "compact size.",
                    "The basic block diagram runs from input devices through a microcontroller "
                    "with processor and memory, out to output devices — a switch and temperature "
                    "sensor in, a fan or buzzer out.",
                ],
            },
            {
                "title": "Working principle",
                "body": [
                    "Sensor, input processing, decision making, output activation. The worked "
                    "example is a temperature sensor feeding a microcontroller that switches a "
                    "fan on. The core advantages are fast response, low power consumption, high "
                    "reliability, compact size and real-time performance.",
                ],
            },
            {
                "title": "Platforms compared",
                "body": [
                    "Arduino Uno is a basic, easy-to-use microcontroller great for learning "
                    "electronics. The ESP32 is a powerful, compact microcontroller with wireless "
                    "communication across home and industrial applications. STM32 offers "
                    "control-intensive communication components. Raspberry Pi is a "
                    "single-board computer capable of master-level tasks.",
                ],
            },
            {
                "title": "Applications and future",
                "body": [
                    "Embedded systems sit inside industrial automation, medical devices, "
                    "washing machines, AC units, robots, smart meters, IoT and smart home "
                    "products, aerospace navigation systems and drones.",
                    "The future runs through Industry 4.0, industrial robotics, artificial "
                    "intelligence, the Internet of Things, autonomous vehicles and smart "
                    "factories — with embedded engineering at the centre of each.",
                ],
            },
        ],
        "gallery": [
            ("embedded-systems/00.jpg", "Complete beginner guide — components, working and future"),
            ("embedded-systems/01.jpg", "STM32-powered climate monitoring solution"),
            ("embedded-systems/02.jpg", "Arduino Uno pinout reference"),
            ("embedded-systems/04.jpg", "MLX90640 32x24 infrared thermal imaging sensor"),
        ],
        "stats": [
            ("4", "Platforms compared"),
            ("4", "Working stages explained"),
            ("5", "Key characteristics defined"),
        ],
    },
    {
        "slug": "sketchbook",
        "title": "Sketchbook",
        "subtitle": "Why I still can't give it up",
        "category": "Practice",
        "year": "2024",
        "tags": "sketch",
        "roles": "Form ideation · Annotation · Daily sketch practice",
        "tools": "Pen and paper — a portable speaker form study",
        "cover": "sketchbook/00.jpg",
        "summary": "A page from the notebook: raw ideation for a portable speaker, and why the "
                   "pen-and-paper habit still drives the process.",
        "intro": [
            "Back to basics: why I still can't give up my sketchbook. For this week's design "
            "snippet I'm closing down the CAD software, putting the digital tablet away, and "
            "going right back to where every decent product starts — just a pen and a bit of paper.",
        ],
        "sections": [
            {
                "title": "It stops you marrying your first idea",
                "body": [
                    "If I jump straight into 3D software, I instinctively start polishing the very "
                    "first thing I build. A sketchbook forces me to churn out ideas fast — testing "
                    "tall and bulky shapes, straight-sided barrels, or softer, fluid lines in a "
                    "matter of minutes.",
                ],
            },
            {
                "title": "It catches the messy thoughts",
                "body": [
                    "The little notes in the margins — 'taller/bulky?', 'flowy', 'grip?' — are "
                    "basically me arguing with myself in real time. It's a quick, permanent log of "
                    "what I was thinking before getting lost in pixels.",
                ],
            },
            {
                "title": "It trains your eye like nothing else",
                "body": [
                    "Doing quick 3D ellipses and shading by hand forces you to really understand "
                    "proportions. If you can make a cylinder look right on paper, you can model "
                    "it properly in CAD. With all the incredible digital tools and AI renderers "
                    "out there today, it's easy to feel like physical sketching is a bit "
                    "old-school — but for me, keeping up this tangible, pen-on-paper habit is a "
                    "massive part of my process.",
                ],
            },
        ],
        "gallery": [
            ("sketchbook/00.jpg", "Notebook page — portable speaker form study and margin notes"),
            ("sketchbook/01.jpg", "Ellipse and volume practice"),
            ("sketchbook/04.jpg", "Ideation detail"),
            ("sketchbook/07.jpg", "Sketch page"),
        ],
        "stats": [
            ("Pen + paper", "No CAD, no tablet"),
            ("2-3", "Sketches posted weekly"),
        ],
    },
    {
        "slug": "form-analysis",
        "title": "Form Analysis & CAD",
        "subtitle": "Toaster breakdown and CAD workflow",
        "category": "Practice",
        "year": "2024",
        "tags": "sketch engineering",
        "roles": "Form analysis · Orthographic and isometric drawing · CAD workflow study",
        "tools": "Sketching · CAD",
        "cover": "form-analysis/00.jpg",
        "summary": "A self-set challenge to post three to four times a week, focused purely on "
                   "sketches and form analysis — starting with a toaster.",
        "intro": [
            "How often do we jump straight into CAD before truly understanding a form? The "
            "strongest designs always start with a fundamental breakdown of shape, proportion "
            "and volume.",
            "That's why I launched a new challenge for myself: posting three to four times a "
            "week focusing purely on sketches and form analysis.",
        ],
        "sections": [
            {
                "title": "Two skill sets, one designer",
                "body": [
                    "Physical sketching is the tactile freedom of pen and paper, where quick "
                    "ideation and raw creativity happen. Digital layouts and CAD are the precision "
                    "toolsets required to translate those ideas into manufacturable reality.",
                    "As modern designers, it's no longer enough to know just one or the other. We "
                    "need to be fluid in both mediums to effectively communicate our intent.",
                ],
            },
            {
                "title": "A robust sketch is built, not drawn",
                "body": [
                    "It follows a strict hierarchy of operations. Phase one, foundation: sketch "
                    "plane, centreline, construction line. Phase two, generation: line, arc, "
                    "circle, ellipse, spline, polygon. Phase three, modification: offset, trim, "
                    "extend, mirror, pattern. Phase four, control: constraint and dimension.",
                ],
            },
            {
                "title": "CAD problems and solutions",
                "body": [
                    "A working reference for the recurring problems a CAD designer faces and how "
                    "to answer them.",
                ],
                "bullets": [
                    "Frequent design changes from customers — prepare a detailed design brief and "
                    "get approval before starting the final design.",
                    "Incorrect measurements and dimensions — verify all measurements and follow "
                    "standard size and manufacturing guidelines.",
                    "Designs difficult to manufacture — coordinate with the production team and "
                    "design to manufacturing capability.",
                    "Tight project deadlines — use time management techniques, CAD templates and "
                    "design libraries to save time.",
                    "Lack of software expertise — attend training and practise advanced tools.",
                    "Slow computers and software crashes — upgrade hardware and optimise files.",
                    "Communication gaps between departments — regular meetings and clear "
                    "documentation.",
                    "File management and version control — naming conventions, backups and cloud "
                    "storage.",
                    "Difficulty creating realistic renders — learn advanced rendering techniques "
                    "and use high-performance systems.",
                    "Keeping up with industry trends — continuous learning and online courses.",
                ],
            },
        ],
        "gallery": [
            ("form-analysis/00.jpg", "Toaster breakdown form analysis"),
            ("form-analysis/01.jpg", "A robust sketch is built, not drawn — four-phase hierarchy"),
            ("form-analysis/02.jpg", "Isometric, perspective and oblique projections"),
            ("form-analysis/03.jpg", "CAD designer problems and solutions"),
        ],
        "stats": [
            ("3-4x", "Posts per week"),
            ("4", "Phases in a structured sketch"),
            ("10", "CAD problems answered"),
        ],
    },
    {
        "slug": "portfolio-deck",
        "title": "Portfolio Deck",
        "subtitle": "The printed book",
        "category": "Self-initiated",
        "year": "2025",
        "tags": "product sketch",
        "roles": "Layout · Sequencing · Writing · Image editing",
        "tools": "Print layout · Adobe suite",
        "cover": "portfolio-deck/00.jpg",
        "summary": "The printed portfolio: four projects — Smart Walker, Coffee Machine, "
                   "Speaker and Drone — sequenced from research to outcome.",
        "intro": [
            "The printed book that collects four projects — Smart Walker, Coffee Machine, "
            "Speaker and Drone — each taken from research and insight through process to "
            "outcome, with the skills and contact pages framing the work.",
        ],
        "sections": [
            {
                "title": "About",
                "body": [
                    "A product design graduate with a keen interest in user-centred design and "
                    "problem solving, skilled in CAD, prototyping and visual communication, and "
                    "passionate about creating functional and aesthetically refined solutions — "
                    "seeking a graduate role in product or industrial design.",
                ],
            },
            {
                "title": "Skills",
                "body": [
                    "Design: user research, concept development, sketching and ideation, "
                    "prototyping. Technical: SOLIDWORKS and Fusion 360, Adobe Illustrator and "
                    "Photoshop, KeyShot rendering. Plus communication and collaborative "
                    "problem solving.",
                ],
            },
            {
                "title": "How it's sequenced",
                "body": [
                    "Each project follows the same rhythm — title, brief, research and insight, "
                    "process, then outcome. Holding the structure constant lets the work itself "
                    "carry the variation, and makes the book readable in a single sitting.",
                ],
            },
        ],
        "gallery": [
            ("portfolio-deck/00.jpg", "Cover — Imaan Rafiq design portfolio"),
            ("portfolio-deck/01.jpg", "Oh, hello there — about me"),
            ("portfolio-deck/02.jpg", "Skills — design, technical and soft"),
            ("portfolio-deck/03.jpg", "Project 1 — Smart Walker, enhancing independent mobility"),
            ("portfolio-deck/04.jpg", "Smart Walker — design scoping and initial prompt sketches"),
            ("portfolio-deck/05.jpg", "Smart Walker — three-phase process"),
            ("portfolio-deck/06.jpg", "Smart Walker — outcome and specifications"),
            ("portfolio-deck/07.jpg", "Project 2 — Coffee machine overview"),
            ("portfolio-deck/08.jpg", "Coffee machine — insight and clay models"),
            ("portfolio-deck/09.jpg", "Coffee machine — interface design iterations"),
            ("portfolio-deck/10.jpg", "Coffee machine — outcome"),
            ("portfolio-deck/11.jpg", "Project 3 — Speaker overview"),
            ("portfolio-deck/12.jpg", "Speaker — concept development"),
            ("portfolio-deck/13.jpg", "Speaker — process: sketches, clay model, internal layout, render"),
            ("portfolio-deck/14.jpg", "Speaker — outcome and reflection"),
            ("portfolio-deck/15.jpg", "Project 4 — Drone brief and storyboard"),
            ("portfolio-deck/16.jpg", "Drone — research, insight and form analysis"),
            ("portfolio-deck/17.jpg", "Drone — process"),
            ("portfolio-deck/18.jpg", "Drone — outcome"),
            ("portfolio-deck/19.jpg", "Contact information"),
            ("portfolio-deck/c1.jpg", "Exploration plates — structure and volumetrics study"),
        ],
        "stats": [
            ("20", "Pages designed"),
            ("4", "Projects sequenced"),
            ("1", "Consistent page rhythm"),
        ],
    },
    {
        "slug": "graduate",
        "title": "Design Engineering Graduand",
        "subtitle": "BSc Product Design & Technology",
        "category": "Background",
        "year": "2025",
        "tags": "engineering product",
        "roles": "SOLIDWORKS · CATIA · Embedded C++ · Lean manufacturing · BOM costing",
        "tools": "Aston University",
        "cover": "graduate/01.jpg",
        "summary": "BSc Product Design & Technology from Aston University — CAD, embedded C++, "
                   "manufacturing and commercial costing in one skill set.",
        "intro": [
            "I graduated with a BSc in Product Design & Technology from Aston University. "
            "My background is a bit of a mix, which I think is genuinely useful.",
        ],
        "sections": [
            {
                "title": "What I bring",
                "body": [],
                "bullets": [
                    "I can design complex parts in Dassault SOLIDWORKS and CATIA",
                    "I can write the embedded C++ code that makes those parts actually do something",
                    "I understand lean manufacturing and supply chains from spending time on the Toyota production floor",
                    "And I can cost a full BOM and build a commercial pricing strategy around it",
                ],
            },
            {
                "title": "Final year project",
                "body": [
                    "My final year project brought all of that together. I built a SmartWalker "
                    "mobility aid from scratch — user research, CAD, electronics, sensor fusion, "
                    "FEA, BOM costing and a 12-section technical report. The kind of project that "
                    "reminded me why I got into engineering in the first place.",
                ],
            },
        ],
        "gallery": [
            ("graduate/01.jpg", "BSc Product Design & Technology — Aston University"),
            ("graduate/00.jpg", "Graduation"),
        ],
        "stats": [
            ("BSc", "Product Design & Technology"),
            ("SOLIDWORKS · CATIA", "CAD platforms"),
            ("C++", "Embedded firmware"),
        ],
    },
    {
        "slug": "aura",
        "title": "Aura",
        "subtitle": "Ultrasonic microcurrent facial contouring system",
        "category": "Ergonomic wellness hardware",
        "year": "2025",
        "tags": "product hardware",
        "roles": "Industrial design · Skin-contact safety · Ergonomics",
        "tools": "Concept sketching · Engineering layout · Anodised CMF",
        "cover": "aura/00.jpg",
        "summary": "High-precision skincare hardware marrying capacitive skin-contact gating, "
                   "3 MHz ultrasonic infusion and biosafe anodised champagne gold electrode nodes.",
        "intro": [
            "A handheld microcurrent facial contouring device that has to feel like a beauty "
            "object while behaving like a piece of regulated hardware.",
            "The brief was ergonomic wellness hardware crossed with beauty tech — the "
            "engineering is invisible, but it is what makes the ritual safe to repeat.",
        ],
        "sections": [
            {
                "title": "Skin-contact gating",
                "body": [
                    "The device only energises its electrodes when it can confirm genuine skin "
                    "contact, using capacitive sensing. That single behaviour is what separates "
                    "a wellness tool from a hazard.",
                ],
            },
            {
                "title": "Ergonomics and the glide plane",
                "body": [
                    "Orthographic pen studies break down the 42-degree anatomical cheek glide "
                    "plane, so the head sits naturally against the face through a full pass "
                    "rather than forcing the wrist to compensate.",
                    "The body is sculpted warm-sand soft-touch silicone with pale rose accents, "
                    "resting on brushed champagne contact electrodes.",
                ],
            },
            {
                "title": "Engineering layout",
                "body": [
                    "Internally the device routes an L-shaped flex PCB around a coin vibration "
                    "motor mount, sealed to IPX7 by a perimeter O-ring gasket and charged from a "
                    "magnetic travertine inductive dock.",
                ],
            },
        ],
        "gallery": [
            ("aura/00.jpg", "Engineering layout sheet — concept sketch, tactile finish and internal flex PCB routing"),
        ],
        "stats": [
            ("3 MHz", "Ultrasonic infusion"),
            ("42°", "Anatomical cheek glide plane"),
            ("IPX7", "Sealing with inductive dock"),
        ],
    },
    {
        "slug": "apothecary",
        "title": "Botanic Rituals",
        "subtitle": "Limited apothecary batch — structure and volumetrics",
        "category": "Packaging design",
        "year": "2025",
        "tags": "product sketch",
        "roles": "Structure design · Volumetrics · Art direction · Typesetting",
        "tools": "Swatch reference · Packaging studies · User ergonomics",
        "cover": "apothecary/00.jpg",
        "summary": "A limited apothecary batch of cold-pressed botanic seed oil — packaging "
                   "structure, volumetrics and swatch reference for a clean apothecary ritual.",
        "intro": [
            "A packaging identity built around the language of a limited apothecary batch: "
            "batch numbers, cold-pressed claims and a ritual you claim rather than buy.",
        ],
        "sections": [
            {
                "title": "Structure and volumetrics",
                "body": [
                    "The primary carton is developed as a structure and volumetrics study, "
                    "resolving how much air the pack can afford to hold before it reads as "
                    "waste on a shelf.",
                ],
            },
            {
                "title": "Texture and swatch reference",
                "body": [
                    "A swatch reference fixes the surface finish, ink behaviour and the "
                    "uncoated stock feel. Formulated to restore vital cellular lipid barriers "
                    "with nutrient-dense active botanicals, the copy stays clinical while the "
                    "palette stays warm.",
                ],
            },
            {
                "title": "The ritual",
                "body": [
                    "A complementary pouch and batch card carry the cold-pressed claim and a "
                    "drop of the seed oil itself, turning the unboxing into the first step of "
                    "the routine rather than an afterthought.",
                ],
            },
        ],
        "gallery": [
            ("apothecary/00.jpg", "Structure and volumetrics — packaging cuts, swatch reference and user ergonomics"),
        ],
        "stats": [
            ("100%", "Cold-pressed botanic seed oil"),
            ("No. 07", "Limited apothecary batch"),
            ("Batch card", "Complementary pouch"),
        ],
    },
    {
        "slug": "med-diag",
        "title": "Med-Diag X1",
        "subtitle": "Handheld biometric triage platform",
        "category": "Medical hardware",
        "year": "2025",
        "tags": "engineering hardware",
        "roles": "Clinical product design · Anthropometrics · Sanitary design",
        "tools": "Medical grade ABS · OLED · Anthropometric study",
        "cover": "med-diag/00.jpg",
        "summary": "A non-invasive clinical diagnostic device unifying PPG optical pulse "
                   "monitoring, contactless infrared thermopiles and a thumb-wheel interface "
                   "for field triage teams.",
        "intro": [
            "Field triage is a one-handed job. Med-Diag X1 is a handheld biometric platform "
            "built for a clinician who is holding a patient, a torch and a deadline at once.",
        ],
        "sections": [
            {
                "title": "Non-invasive sensing",
                "body": [
                    "PPG optical pulse monitoring and contactless infrared thermopiles let the "
                    "device read vitals without breaking skin, which matters enormously when a "
                    "patient has to be assessed quickly in the field.",
                ],
            },
            {
                "title": "Product realisation",
                "body": [
                    "A sanitary matte white antimicrobial casing carries a high-contrast "
                    "clinical OLED interface, framed to stay legible in daylight and easy to "
                    "wipe down between patients.",
                ],
            },
            {
                "title": "Anthropometric study",
                "body": [
                    "The thumb-wheel control was placed by calculating the single-handed thumb "
                    "sweep across the 5th to 95th percentile hand reach, with internal thermal "
                    "cutaways keeping the electronics within safe limits.",
                ],
            },
        ],
        "gallery": [
            ("med-diag/00.jpg", "Product realisation — clinical field device and 5th-95th percentile anthropometric study"),
        ],
        "stats": [
            ("PPG", "Optical pulse monitoring"),
            ("IR", "Contactless thermopiles"),
            ("5th-95th", "Hand percentile reach"),
        ],
    },
]

CATEGORIES = [
    ("product", "Product"),
    ("engineering", "Engineering"),
    ("ux", "Digital"),
    ("sketch", "Form & sketch"),
    ("hardware", "Electronics"),
    ("others", "Other"),
]