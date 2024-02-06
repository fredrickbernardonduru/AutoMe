import Link from "next/link";
import ThemeToggle from "../ThemeToggle";

export default function Navbar() {
  return (
    <header className="sticky top-0 bg-background">
      <div className="gap3 mx-auto flex max-w-3xl flex-wrap justify-between px-4 py-3">
        <nav className="space-x-4 font-medium">
          <Link href="/">Home</Link>
          <Link href="/about">About me</Link>
          <Link href="/social">Social media</Link>
        </nav>
        <div>
          <ThemeToggle />
        </div>
      </div>
    </header>
  );
}
