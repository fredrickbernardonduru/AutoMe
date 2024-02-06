import Link from "next/link";

export default function Navbar() {
    return <header className="sticky top-0 bg-background">
        <div className="max-w-3xl mx-auto flex flex-wrap justify-between gap3 py-3 px-4">
          <nav className="space-x-4 font-medium">
            <Link href="/">Home</Link>
            <Link href="/about">About me</Link>
            <Link href="/social">Social media</Link>
            </nav>  
        </div>

    </header>
}